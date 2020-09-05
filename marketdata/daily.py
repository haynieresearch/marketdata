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
        sma = get_tech("SMA",symbol,api_key,api_base)
        macd_hist = get_tech("MACD",symbol,api_key,api_base)
        print(macd_hist)
        #ema = get_tech("EMA",symbol,api_key,api_base)
        #macd = numtest(get_tech("MACD",symbol,api_key,api_base)["MACD"])
        #macd_hist = numtest(get_tech("MACD",symbol,api_key,api_base)["MACD_Hist"])
        #macd_signal = numtest(get_tech("MACD",symbol,api_key,api_base)["MACD_Signal"])
        #stoch_slowk = numtest(get_tech("STOCH",symbol,api_key,api_base)["SlowK"])
        #stoch_slowd = numtest(get_tech("STOCH",symbol,api_key,api_base)["SlowD"])
        #rsi = numtest(get_tech("RSI",symbol,api_key,api_base,data_date)["RSI"])
        #stochrsi_fastk = numtest(get_tech("STOCHRSI",symbol,api_key,api_base)["FastK"])
        #stochrsi_fastd = numtest(get_tech("STOCHRSI",symbol,api_key,api_base)["FastD"])
        #willr = numtest(get_tech("WILLR",symbol,api_key,api_base,data_date)["WILLR"])
        #bbands_upper = numtest(get_tech("BBANDS",symbol,api_key,api_base)["Real Upper Band"])
        #bbands_lower = numtest(get_tech("BBANDS",symbol,api_key,api_base)["Real Lower Band"])
        #bbands_middle = numtest(get_tech("BBANDS",symbol,api_key,api_base)["Real Middle Band"])
        #roc = numtest(get_tech("ROC",symbol,api_key,api_base)["ROC"])
        #rocr = numtest(get_tech("ROCR",symbol,api_key,api_base)["ROCR"])

    except Exception as e:
        print('Error: {}'.format(str(e)))

def update(date):
    print("Updating Daily Data")
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            price(uuid, symbol)
            #technical(uuid, symbol)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()
