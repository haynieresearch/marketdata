#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		STATS.PY
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
import requests
from datetime import date
from .settings import settings_data
from .database import db,dw
from .functions import numtest

logging.basicConfig(format='%(levelname)s - %(message)s', level=settings_data['global']['loglevel'])

api_base = settings_data['datasources']['IEX']['url']
api_key = settings_data['datasources']['IEX']['key']

session = requests.Session()

def stats(uuid,symbol):
    logging.debug("Processing stats data for: " + symbol + ".")

    cursor = db.cursor()
    try:
        api = f"{api_base}/stock/{symbol}/stats?token={api_key}"
        #response_data = json.loads(urlreq.urlopen(api).read().decode())
        response_data = session.get(api).json()

        companyName         = response_data['companyName']
        marketcap           = numtest(response_data['marketcap'])
        week52high          = numtest(response_data['week52high'])
        week52low           = numtest(response_data['week52low'])
        week52change        = numtest(response_data['week52change'])
        sharesOutstanding   = numtest(response_data['sharesOutstanding'])
        avg10Volume         = numtest(response_data['avg10Volume'])
        avg30Volume         = numtest(response_data['avg30Volume'])
        day200MovingAvg     = numtest(response_data['day200MovingAvg'])
        day50MovingAvg      = numtest(response_data['day50MovingAvg'])
        employees           = numtest(response_data['employees'])
        ttmEPS              = numtest(response_data['ttmEPS'])
        ttmDividendRate     = numtest(response_data['ttmDividendRate'])
        dividendYield       = numtest(response_data['dividendYield'])
        nextDividendDate    = response_data['nextDividendDate']
        if nextDividendDate is None or nextDividendDate == "":
                nextDividendDate = "0000-00-00"
        exDividendDate      = response_data['exDividendDate']
        if exDividendDate is None or exDividendDate == "":
                exDividendDate = "0000-00-00"
        nextEarningsDate    = response_data['nextEarningsDate']
        if nextEarningsDate is None or nextEarningsDate == "":
                nextEarningsDate = "0000-00-00"
        peRatio             = numtest(response_data['peRatio'])
        beta                = numtest(response_data['beta'])
        maxChangePercent    = numtest(response_data['maxChangePercent'])
        year5ChangePercent  = numtest(response_data['year5ChangePercent'])
        year2ChangePercent  = numtest(response_data['year2ChangePercent'])
        year1ChangePercent  = numtest(response_data['year1ChangePercent'])
        ytdChangePercent    = numtest(response_data['ytdChangePercent'])
        month6ChangePercent = numtest(response_data['month6ChangePercent'])
        month3ChangePercent = numtest(response_data['month3ChangePercent'])
        month1ChangePercent = numtest(response_data['month1ChangePercent'])
        day30ChangePercent  = numtest(response_data['day30ChangePercent'])
        day5ChangePercent   = numtest(response_data['day5ChangePercent'])
        updated_date        = date.today()

        try:
            sql = f"""
            INSERT INTO
            stats(
                security_id,
                companyName,
                marketcap,
                week52high,
                week52low,
                week52change,
                sharesOutstanding,
                avg10Volume,
                avg30Volume,
                day200MovingAvg,
                day50MovingAvg,
                employees,
                ttmEPS,
                ttmDividendRate,
                dividendYield,
                nextDividendDate,
                exDividendDate,
                nextEarningsDate,
                peRatio,
                beta,
                maxChangePercent,
                year5ChangePercent,
                year2ChangePercent,
                year1ChangePercent,
                ytdChangePercent,
                month6ChangePercent,
                month3ChangePercent,
                month1ChangePercent,
                day30ChangePercent,
                day5ChangePercent,
                updated_date)
            values(
                {uuid},
                '{companyName}',
                {marketcap},
                {week52high},
                {week52low},
                {week52change},
                {sharesOutstanding},
                {avg10Volume},
                {avg30Volume},
                {day200MovingAvg},
                {day50MovingAvg},
                {employees},
                {ttmEPS},
                {ttmDividendRate},
                {dividendYield},
                '{nextDividendDate}',
                '{exDividendDate}',
                '{nextEarningsDate}',
                {peRatio},
                {beta},
                {maxChangePercent},
                {year5ChangePercent},
                {year2ChangePercent},
                {year1ChangePercent},
                {ytdChangePercent},
                {month6ChangePercent},
                {month3ChangePercent},
                {month1ChangePercent},
                {day30ChangePercent},
                {day5ChangePercent},
                '{updated_date}');
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
    current_date = date.today()

    try:
        dw_cursor.execute(f"SELECT uuid, symbol FROM security WHERE uuid NOT IN (select security_id from stats where updated_date = '{current_date}')")
        results = dw_cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            stats(uuid, symbol)

    except Exception as e:
        logging.error(format(str(e)))
        sys.exit(1)
    dw.close()
