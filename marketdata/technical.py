#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-20
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		TECHNICAL.PY
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

def get_tech(ind,symbol,api_key,base,date):
    try:
        api = base + f"{ind}" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        data = json.loads(urlreq.urlopen(api).read().decode())
    except Exception as e:
        print("Error with API call.")
        print(e)

    try:
        json_txt = f"Technical Analysis: {ind}"
        data = data[json_txt][date]
    except Exception as e:
        print("Error assigning API variable.")
        print(e)
    return data

def update_technical(uuid,symbol,date):
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()

    try:
        cursor.execute(f"select security_id from technical where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        try:
            sma = numtest(get_tech("SMA",symbol,api_key,api_base,data_date)["SMA"])
            ema = numtest(get_tech("EMA",symbol,api_key,api_base,data_date)["EMA"])
            macd = numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD"])
            macd_hist = numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD_Hist"])
            macd_signal = numtest(get_tech("MACD",symbol,api_key,api_base,data_date)["MACD_Signal"])
            stoch_slowk = numtest(get_tech("STOCH",symbol,api_key,api_base,data_date)["SlowK"])
            stoch_slowd = numtest(get_tech("STOCH",symbol,api_key,api_base,data_date)["SlowD"])
            rsi = numtest(get_tech("RSI",symbol,api_key,api_base,data_date)["RSI"])
            stochrsi_fastk = numtest(get_tech("STOCHRSI",symbol,api_key,api_base,data_date)["FastK"])
            stochrsi_fastd = numtest(get_tech("STOCHRSI",symbol,api_key,api_base,data_date)["FastD"])
            willr = numtest(get_tech("WILLR",symbol,api_key,api_base,data_date)["WILLR"])
            bbands_upper = numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Upper Band"])
            bbands_lower = numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Lower Band"])
            bbands_middle = numtest(get_tech("BBANDS",symbol,api_key,api_base,data_date)["Real Middle Band"])
            roc = numtest(get_tech("ROC",symbol,api_key,api_base,data_date)["ROC"])
            rocr = numtest(get_tech("ROCR",symbol,api_key,api_base,data_date)["ROCR"])
        except Exception as e:
            print("Error assigning variables.")
            print(e)

        if response == None:
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
                print("Adding " + symbol + " technical data to database.")
            except Exception as e:
                print("Error Adding " + symbol + " technical data to database.")
                print(e)
        else:
            sql = f"""
                UPDATE technical SET sma = {sma},
                ema = {ema},
                macd = {macd},
                macd_signal = {macd_signal},
                macd_hist = {macd_hist},
                stoch_slow_d = {stoch_slowd},
                stoch_slow_k = {stoch_slowk},
                rsi = {rsi},
                stochrsi_fast_k = {stochrsi_fastk},
                stochrsi_fast_d = {stochrsi_fastd},
                willr = {willr},
                roc = {roc},
                rocr = {rocr},
                bbands_lower = {bbands_lower},
                bbands_upper = {bbands_upper},
                bbands_middle = {bbands_middle}
                WHERE security_id = {uuid} AND date = '{sql_date}';
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Updating " + symbol + " technical data in database.")
            except Exception as e:
                print("Error updating " + symbol + " technical data in database.")
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
            update_technical(uuid, symbol, date)
            time.sleep(1)

    except Exception as e:
        print(e)
    db.close()

def update_segment(segment, date):
    cursor = db.cursor()
    try:
        cursor.execute(f"select uuid, symbol from security_segment where segment = '{segment}'")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_technical(uuid, symbol, date)
            time.sleep(1)

    except Exception as e:
        print(e)
    db.close()
