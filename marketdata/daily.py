#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-20
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		DAILY.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-08-20 - LHAYNIE - INITIAL VERSION
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
from .settings import settings_data
from .database import db,dw
from .functions import numtest

api_base    = settings_data['datasources']['AlphaVantage']['url']
api_key     = settings_data['datasources']['AlphaVantage']['key']
obs         = settings_data['datasources']['AlphaVantage']['obs']

def daily(uuid,symbol):
    cursor = db.cursor()
    try:
        api = f"{api_base}TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=compact&apikey={api_key}"

        response_data = json.loads(urlreq.urlopen(api).read().decode('utf-8'))
        response_data = response_data['Time Series (Daily)']
        response_data = dict(list(response_data.items())[0: obs])

        for key,value in response_data.items():
            dailyDate        = key + " 00:00:00"
            dailyOpen        = numtest(value['1. open'])
            dailyHigh        = numtest(value['2. high'])
            dailyLow         = numtest(value['3. low'])
            dailyClose       = numtest(value['4. close'])
            dailyAdjClose    = numtest(value['5. adjusted close'])
            dailyVolume      = numtest(value['6. volume'])
            dailyDivAmt      = numtest(value['7. dividend amount'])
            dailySplit_c     = numtest(value['8. split coefficient'])

            try:
                sql = f"""
                INSERT INTO
                daily (
                    security_id,
                    date,
                    open,
                    high,
                    low,
                    close,
                    adj_close,
                    volume,
                    div_amt,
                    split_c)
                values(
                    {uuid},
                    '{dailyDate}',
                    {dailyOpen},
                    {dailyHigh},
                    {dailyLow},
                    {dailyClose},
                    {dailyAdjClose},
                    {dailyVolume},
                    {dailyDivAmt},
                    {dailySplit_c});
                """
                try:
                    cursor.execute(sql)
                    db.commit()
                except Exception as e:
                    print('Error: {}'.format(str(e)))

            except Exception as e:
                print('Error: {}'.format(str(e)))

    except Exception as e:
        print('Error: {}'.format(str(e)))

def update():
    dw_cursor = dw.cursor()
    try:
        dw_cursor.execute("select uuid, symbol from security")
        results = dw_cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            daily(uuid, symbol)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    dw.close()

def update_segment(segment):
    dw_cursor = dw.cursor()
    try:
        dw_cursor.execute(f"select uuid, symbol from security_segment where segment = '{segment}'")
        results = dw_cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            daily(uuid, symbol)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    dw.close()
