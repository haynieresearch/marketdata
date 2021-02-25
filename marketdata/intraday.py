#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		INTRADAY.PY
#**********************************************************
#ETL Stock Market Data
#Copyright 2020 Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
import sys
import urllib.request as urlreq
import json
import pandas as pd
import logging
from .settings import settings_data
from .database import db,dw
from .functions import numtest

logging.basicConfig(format='%(levelname)s - %(message)s', level=settings_data['global']['loglevel'])

api_base = settings_data['datasources']['IEX']['url']
api_key = settings_data['datasources']['IEX']['key']

def intraday(uuid,symbol):
    logging.debug("Processing hourly data for: " + symbol + ".")

    cursor = db.cursor()
    try:
        api = f"{api_base}/stock/{symbol}/intraday-prices?token={api_key}&chartInterval=60&chartLast=1"
        response_data = json.loads(urlreq.urlopen(api).read().decode())

        date                    = response_data[0]['date']
        minute                  = response_data[0]['minute']
        label                   = response_data[0]['label']
        high                    = numtest(response_data[0]['high'])
        low                     = numtest(response_data[0]['low'])
        open                    = numtest(response_data[0]['open'])
        close                   = numtest(response_data[0]['close'])
        average                 = numtest(response_data[0]['average'])
        volume                  = numtest(response_data[0]['volume'])
        notional                = numtest(response_data[0]['notional'])
        numberOfTrades          = numtest(response_data[0]['numberOfTrades'])

        if close > 0:
            try:
                sql = f"""
                INSERT INTO
                intraday(
                    security_id,
                    `symbol`,
                    `date`,
                    `minute`,
                    label,
                    high,
                    low,
                    `open`,
                    `close`,
                    average,
                    volume,
                    notional,
                    numberOfTrades)
                values(
                    {uuid},
                    '{symbol}',
                    '{date}',
                    '{minute}',
                    '{label}',
                    {high},
                    {low},
                    {open},
                    {close},
                    {average},
                    {volume},
                    {notional},
                    {numberOfTrades});
                """

                try:
                    cursor.execute(sql)
                    db.commit()
                except Exception as e:
                    error = format(str(e))
                    if error.find("Duplicate entry") != -1:
                        logging.debug("Data already exists for " + symbol + " on date " + data_date + ".")
                    else:
                        logging.error(format(str(e)))

            except Exception as e:
                logging.error(format(str(e)))

    except Exception as e:
        logging.error(format(str(e)))

def update():
    dw_cursor = dw.cursor()

    try:
        dw_cursor.execute("""SELECT distinct security_id as uuid,symbol FROM marketdata.daily a
                             left join security b on a.security_id = b.uuid
                             where date >= date_sub(now(),interval 30 day)""")
        results = dw_cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            intraday(uuid, symbol)

    except Exception as e:
        logging.error(format(str(e)))
        sys.exit(1)
    dw.close()
