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
from .settings import settings_data
from .database import db
from .functions import numtest

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def price(uuid,symbol,date):
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from price where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        if response == None:
            api = f"{api_base}TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

            response_data = json.loads(urlreq.urlopen(api).read().decode('utf-8'))
            response_data = response_data['Time Series (Daily)'][date]

            open        = functions.numtest(response_data['1. open'])
            high        = functions.numtest(response_data['2. high'])
            low         = functions.numtest(response_data['3. low'])
            close       = functions.numtest(response_data['4. close'])
            adj_close   = functions.numtest(response_data['5. adjusted close'])
            volume      = functions.numtest(response_data['6. volume'])
            div_amt     = functions.numtest(response_data['7. dividend amount'])
            split_c     = functions.numtest(response_data['8. split coefficient'])

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
                print("Adding " + symbol + " price data to database for " + data_date + ".")
            except Exception as e:
                print("Error adding " + symbol + " price data to database for " + data_date + ".")
                print(e)
        else:
            print(symbol + " already in daily data in database for " + data_date + ".")

    except Exception as e:
        print("Error! " + symbol)
        print('Error: {}'.format(str(e)))
    #time.sleep(1)

def get_tech(ind,symbol,api_key,base,date):
    try:
        api = base + f"{ind}" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        data = json.loads(urlreq.urlopen(api).read().decode())
    except Exception as e:
        print("Error with API call.")
        print('Error: {}'.format(str(e)))

    try:
        json_txt = f"Technical Analysis: {ind}"
        data = data[json_txt][date]
    except Exception as e:
        print("Error assigning API variable.")
        print('Error: {}'.format(str(e)))
    #time.sleep(1)
    return data

def technical(uuid,symbol,date):
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()

    try:
        cursor.execute(f"select security_id from technical where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        if response == None:
            try:
                sma = functions.numtest(get_tech("SMA",symbol,api_key,api_base,data_date)["SMA"])
                ema = functions.numtest(get_tech("EMA",symbol,api_key,api_base,data_date)["EMA"])
                macd = functions.numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD"])
                macd_hist = functions.numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD_Hist"])
                macd_signal = functions.numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD_Signal"])
                stoch_slowk = functions.numtest(get_tech("STOCH",symbol,api_key,api_base,data_date)["SlowK"])
                stoch_slowd = functions.numtest(get_tech("STOCH",symbol,api_key,api_base,data_date)["SlowD"])
                rsi = functions.numtest(get_tech("RSI",symbol,api_key,api_base,data_date)["RSI"])
                stochrsi_fastk = functions.numtest(get_tech("STOCHRSI",symbol,api_key,api_base,data_date)["FastK"])
                stochrsi_fastd = functions.numtest(get_tech("STOCHRSI",symbol,api_key,api_base,data_date)["FastD"])
                willr = functions.numtest(get_tech("WILLR",symbol,api_key,api_base,data_date)["WILLR"])
                bbands_upper = functions.numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Upper Band"])
                bbands_lower = functions.numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Lower Band"])
                bbands_middle = functions.numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Middle Band"])
                roc = functions.numtest(get_tech("ROC",symbol,api_key,api_base,data_date)["ROC"])
                rocr = functions.numtest(get_tech("ROCR",symbol,api_key,api_base,data_date)["ROCR"])
            except Exception as e:
                print("Error assigning variables.")
                print('Error: {}'.format(str(e)))

            sql = f"""
                INSERT INTO
                technical (
                    security_id,
                    date,
                    sma,
                    ema,
                    macd,
                    macd_signal,
                    macd_hist,
                    stoch_slow_d,
                    stoch_slow_k,
                    rsi,
                    stochrsi_fast_k,
                    stochrsi_fast_d,
                    willr,
                    roc,
                    rocr,
                    bbands_lower,
                    bbands_upper,
                    bbands_middle)
                values(
                    {uuid},
                    '{sql_date}',
                    {sma},
                    {ema},
                    {macd},
                    {macd_signal},
                    {macd_hist},
                    {stoch_slowd},
                    {stoch_slowk},
                    {rsi},
                    {stochrsi_fastk},
                    {stochrsi_fastd},
                    {willr},
                    {roc},
                    {rocr},
                    {bbands_lower},
                    {bbands_upper},
                    {bbands_middle});
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Adding " + symbol + " technical data to database for " + data_date + ".")
            except Exception as e:
                print("Error Adding " + symbol + " technical data to database for " + data_date + ".")
                print('Error: {}'.format(str(e)))
        else:
            print(symbol + " already in technical data in database for " + data_date + ".")

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
            price(uuid, symbol, date)
            technical(uuid, symbol, date)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()

def update_segment(segment,date):
    print("Updating Daily Data")
    cursor = db.cursor()
    try:
        cursor.execute(f"select uuid, symbol from security_segment where segment = '{segment}'")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            price(uuid, symbol, date)
            technical(uuid, symbol, date)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()
