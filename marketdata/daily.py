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
import time
import urllib.request as urlreq
import json
from datetime import date, datetime, timedelta
from .settings import settings_data
from .database import db

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def numtest(input):
    if isinstance(input, float) == True:
        input = input
    elif isinstance(input, int) == True:
        input = input
    else:
        try:
            input = float(input)
        except:
            input = 0
    return input

def update_daily(uuid,symbol,date):
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from price where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        api = f"{api_base}TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"
        response_data = json.loads(urlreq.urlopen(api).read().decode('utf-8'))
        response_data = response_data['Time Series (Daily)'][date]

        open        = numtest(response_data['1. open'])
        high        = numtest(response_data['2. high'])
        low         = numtest(response_data['3. low'])
        close       = numtest(response_data['4. close'])
        adj_close   = numtest(response_data['5. adjusted close'])
        volume      = numtest(response_data['6. volume'])
        div_amt     = numtest(response_data['7. dividend amount'])
        split_c     = numtest(response_data['8. split coefficient'])

        if response == None:
            sql = f"""
                INSERT INTO
                price (
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
                    '{sql_date}',
                    {open},
                    {high},
                    {low},
                    {close},
                    {adj_close},
                    {volume},
                    {div_amt},
                    {split_c});
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Adding " + symbol + " price data to database.")
            except Exception as e:
                print("Error adding " + symbol)
                print(e)
        else:
            sql = f"""
                UPDATE price SET open = {open},
                high = {high},
                low = {low},
                close = {close},
                adj_close = {adj_close},
                volume = {volume},
                div_amt = {div_amt},
                split_c = {split_c}
                WHERE security_id = {uuid} AND date = '{sql_date}';
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Updating " + symbol + " daily data in database.")
            except Exception as e:
                print("Error updating " + symbol)
                print(e)

    except Exception as e:
        print("Error! " + symbol)
        print(e)

def update(date):
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_daily(uuid, symbol, date)
            time.sleep(1)

    except Exception as e:
        print(e)
    db.close()

def update_segment(segment,date):
    cursor = db.cursor()
    try:
        cursor.execute(f"select uuid, symbol from security_segment where segment = '{segment}'")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_daily(uuid, symbol, date)
            time.sleep(1)

    except Exception as e:
        print(e)
    db.close()
