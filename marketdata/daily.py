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
import urllib.request as urlreq
import json
from re import search
from datetime import date, datetime, timedelta
from .settings import *
from .database import *

api_base = settings_data['datasources']['IEX']['url']
api_key = settings_data['datasources']['IEX']['key']

def numtest(input):
    if isinstance(input, float) == True:
        input = input
    elif isinstance(input, int) == True:
        input = input
    else:
        input = 0
    return input

def update_daily(uuid,symbol,date):
    api_date = date.replace('-', '')
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from price where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        api = f"{api_base}/stock/{symbol}/chart/date/{api_date}?token={api_key}"
        response_data = json.loads(urlreq.urlopen(api).read().decode())
        response_data = response_data[-1]

        high                    = numtest(response_data['high'])
        low                     = numtest(response_data['low'])
        average                 = numtest(response_data['average'])
        volume                  = numtest(response_data['volume'])
        notional                = numtest(response_data['notional'])
        num_trades              = numtest(response_data['numberOfTrades'])
        market_high             = numtest(response_data['marketHigh'])
        market_low              = numtest(response_data['marketLow'])
        market_avg              = numtest(response_data['marketAverage'])
        market_volume           = numtest(response_data['marketVolume'])
        market_notional         = numtest(response_data['marketNotional'])
        market_num_trades       = numtest(response_data['marketNumberOfTrades'])
        open                    = numtest(response_data['open'])
        close                   = numtest(response_data['close'])
        market_open             = numtest(response_data['marketOpen'])
        market_close            = numtest(response_data['marketClose'])
        change_over_time        = numtest(response_data['changeOverTime'])
        market_change_over_time = numtest(response_data['marketChangeOverTime'])

        if response == None:
            sql = f"""
                INSERT INTO
                price (
                    security_id,
                    date,
                    high,
                    low,
                    average,
                    volume,
                    notional,
                    num_trades,
                    market_high,
                    market_low,
                    market_avg,
                    market_volume,
                    market_notional,
                    market_num_trades,
                    open,
                    close,
                    market_open,
                    market_close,
                    change_over_time,
                    market_change_over_time)
                values(
                    {uuid},
                    '{sql_date}',
                    {high},
                    {low},
                    {average},
                    {volume},
                    {notional},
                    {num_trades},
                    {market_high},
                    {market_low},
                    {market_avg},
                    {market_volume},
                    {market_notional},
                    {market_num_trades},
                    {open},
                    {close},
                    {market_open},
                    {market_close},
                    {change_over_time},
                    {market_change_over_time});
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Adding " + symbol + " price data to database.")
            except Exception as e:
                print(e)
        else:
            sql = f"""
                UPDATE price SET high = {high},
                low = {low},
                average = {average},
                volume = {volume},
                notional = {notional},
                num_trades = {num_trades},
                market_high = {market_high},
                market_low = {market_low},
                market_avg = {market_avg},
                market_volume = {market_volume},
                market_notional = {market_notional},
                market_num_trades = {market_num_trades},
                open = {open},
                close = {close},
                market_open = {market_open},
                market_close = {market_close},
                change_over_time = {change_over_time},
                market_change_over_time = {market_change_over_time}
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

def update(date):
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_daily(uuid, symbol, date)

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

    except Exception as e:
        print(e)
    db.close()
