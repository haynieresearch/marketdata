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
from .database import db
from .functions import numtest

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def price(uuid,symbol):
    cursor = db.cursor()
    try:
        api = f"{api_base}TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

        response_data = json.loads(urlreq.urlopen(api).read().decode('utf-8'))
        response_data = response_data['Time Series (Daily)']

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
    #time.sleep(1)

def get_tech(ind,symbol,api_key,base):
    try:
        api = base + f"{ind}" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        data = json.loads(urlreq.urlopen(api).read().decode())
    except Exception as e:
        print('Error: {}'.format(str(e)))

    try:
        json_txt = f"Technical Analysis: {ind}"
        data = data[json_txt]
    except Exception as e:
        print('Error: {}'.format(str(e)))
    return data

def technical(uuid,symbol):
    cursor = db.cursor()

    try:
        sma = pd.DataFrame.from_dict(get_tech("SMA",symbol,api_key,api_base))
        ema = pd.DataFrame.from_dict(get_tech("EMA",symbol,api_key,api_base))
        macd = pd.DataFrame.from_dict(get_tech("MACD",symbol,api_key,api_base))
        stoch = pd.DataFrame.from_dict(get_tech("STOCH",symbol,api_key,api_base))
        rsi = pd.DataFrame.from_dict(get_tech("RSI",symbol,api_key,api_base))
        stochrsi = pd.DataFrame.from_dict(get_tech("STOCHRSI",symbol,api_key,api_base))
        willr = pd.DataFrame.from_dict(get_tech("WILLR",symbol,api_key,api_base))
        bbands = pd.DataFrame.from_dict(get_tech("BBANDS",symbol,api_key,api_base))
        roc = pd.DataFrame.from_dict(get_tech("ROC",symbol,api_key,api_base))
        rocr = pd.DataFrame.from_dict(get_tech("ROCR",symbol,api_key,api_base))

        tech_data = [sma,ema,macd,stoch,rsi,stochrsi,willr,bbands,roc,rocr]
        technical = pd.concat(tech_data)

        print(technical.transpose())

    except Exception as e:
        print('Error: {}'.format(str(e)))

def update(date):
    print("Updating Daily Data")
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security limit 1")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            #price(uuid, symbol)
            technical(uuid, symbol)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()
