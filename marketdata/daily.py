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
import os
import sys
import urllib.request as urlreq
import json
from re import search
from datetime import date, datetime, timedelta
from .settings import *
from .database import *

today = date.today() - timedelta(days = 1)
now = datetime.now()
data_date = today.strftime("%Y-%m-%d")
sql_date = data_date + " 00:00:00"

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def update_daily(uuid,symbol):
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from price where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        api_function = "TIME_SERIES_DAILY_ADJUSTED"
        api = api_base + api_function + "&symbol=" + symbol + "&apikey=" + api_key

        try:
            data = json.loads(urlreq.urlopen(api).read().decode())
            if len(data)==0:
                print("Error updating " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(data)):
                print("Error updating " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        daily_data = data[[i for i in data.keys() if 'Time Series (Daily)' in i][0]]

        if list(daily_data.keys())[0] != data_date:
            print("Error updating " + symbol + ", API responded with incorrect date.")
            return

        open = daily_data[data_date]['1. open']
        high = daily_data[data_date]['2. high']
        low = daily_data[data_date]['3. low']
        close = daily_data[data_date]['4. close']
        adj_close = daily_data[data_date]['5. adjusted close']
        volume = daily_data[data_date]['6. volume']
        div_amt = daily_data[data_date]['7. dividend amount']
        split_c = daily_data[data_date]['8. split coefficient']

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
                    div_amount,
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
                print("Adding " + symbol + " daily data to database.")
            except Exception as e:
                print(e)
        else:
            sql = f"""
                UPDATE price SET open = {open},
                high = {high},
                low = {low},
                close = {close},
                adj_close = {adj_close},
                volume = {volume},
                div_amount = {div_amt},
                split_c = {split_c}
                WHERE security_id = {uuid} AND date = '{sql_date}';
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Updating " + symbol + " daily data in database.")
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

def update():
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_daily(uuid, symbol)

    except Exception as e:
        print(e)
    db.close()
