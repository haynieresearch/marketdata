#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		HISTORY.PY
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

def history(uuid,symbol,api_date,sql_date):
    logging.debug("Processing historical data for: " + symbol + ".")

    cursor = db.cursor()
    try:
        api = f"{api_base}/stock/{symbol}/chart/date/{api_date}?chartByDay=true&token={api_key}"
        response_data = json.loads(urlreq.urlopen(api).read().decode())

        open            = numtest(response_data[0]['open'])
        high            = numtest(response_data[0]['high'])
        low             = numtest(response_data[0]['low'])
        close           = numtest(response_data[0]['close'])
        volume          = numtest(response_data[0]['volume'])
        uOpen           = numtest(response_data[0]['uOpen'])
        uHigh           = numtest(response_data[0]['uHigh'])
        uLow            = numtest(response_data[0]['uLow'])
        uClose          = numtest(response_data[0]['uClose'])
        uVolume         = numtest(response_data[0]['uVolume'])
        fOpen           = numtest(response_data[0]['fOpen'])
        fHigh           = numtest(response_data[0]['fHigh'])
        fLow            = numtest(response_data[0]['fLow'])
        fClose          = numtest(response_data[0]['fClose'])
        fVolume         = numtest(response_data[0]['fVolume'])
        change          = numtest(response_data[0]['change'])
        changePercent   = numtest(response_data[0]['changePercent'])

        try:
            sql = f"""
            INSERT INTO
            daily(
                security_id,
                date,
                open,
                high,
                low,
                close,
                volume,
                uOpen,
                uHigh,
                uLow,
                uClose,
                uVolume,
                fOpen,
                fHigh,
                fLow,
                fClose,
                fVolume,
                `change`,
                changePercent)
            values(
                {uuid},
                '{sql_date}',
                {open},
                {high},
                {low},
                {close},
                {volume},
                {uOpen},
                {uHigh},
                {uLow},
                {uClose},
                {uVolume},
                {fOpen},
                {fHigh},
                {fLow},
                {fClose},
                {fVolume},
                {change},
                {changePercent});
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

def update(date):
    api_date = date.replace('-', '')
    sql_date = date + " 00:00:00"

    dw_cursor = dw.cursor()

    try:
        dw_cursor.execute(f"SELECT uuid, symbol FROM security WHERE uuid NOT IN (select security_id from daily where date = '{sql_date}')")
        results = dw_cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            history(uuid, symbol, api_date, sql_date)

    except Exception as e:
        logging.error(format(str(e)))
        sys.exit(1)
    dw.close()
