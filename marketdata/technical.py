#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-09-05
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		TECHNICAL.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-09-05 - LHAYNIE - INITIAL VERSION
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
import threading
from .settings import settings_data
from .database import db,dw
from .functions import numtest

api_base    = settings_data['datasources']['AlphaVantage']['url']
api_key     = settings_data['datasources']['AlphaVantage']['key']
obs         = settings_data['datasources']['AlphaVantage']['obs']

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

def update_tech(indicator,symbol):
    if indicator == "SMA":
        global sma
        sma = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "EMA":
        global ema
        ema = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "MACD":
        global macd
        macd = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "STOCH":
        global stoch
        stoch = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "RSI":
        global rsi
        rsi = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "STOCHRSI":
        global stochrsi
        stochrsi = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "WILLR":
        global willr
        willr = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "BBANDS":
        global bbands
        bbands = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "ROC":
        global roc
        roc = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))
    elif indicator == "ROCR":
        global rocr
        rocr = pd.DataFrame.from_dict(get_tech(indicator,symbol,api_key,api_base))

def technical(uuid,symbol):
    cursor = db.cursor()

    try:
        t0 = threading.Thread(target=update_tech, args=("SMA",symbol))
        t1 = threading.Thread(target=update_tech, args=("EMA",symbol))
        t2 = threading.Thread(target=update_tech, args=("MACD",symbol))
        t3 = threading.Thread(target=update_tech, args=("STOCH",symbol))
        t4 = threading.Thread(target=update_tech, args=("RSI",symbol))
        t5 = threading.Thread(target=update_tech, args=("STOCHRSI",symbol))
        t6 = threading.Thread(target=update_tech, args=("WILLR",symbol))
        t7 = threading.Thread(target=update_tech, args=("BBANDS",symbol))
        t8 = threading.Thread(target=update_tech, args=("ROC",symbol))
        t9 = threading.Thread(target=update_tech, args=("ROCR",symbol))

        t0.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        t0.join()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

        tech_data = [sma,ema,macd,stoch,rsi,stochrsi,willr,bbands,roc,rocr]
        technical = pd.concat(tech_data)
        technical = json.loads(technical.to_json())
        technical = dict(list(technical.items())[0: obs])

        for key,value in technical.items():
            techdate = key + " 00:00:00"
            techsma = numtest(value['SMA'])
            techema = numtest(value['EMA'])
            techmacd = numtest(value['MACD'])
            techmacd_hist = numtest(value['MACD_Hist'])
            techmacd_signal = numtest(value['MACD_Signal'])
            techslowk = numtest(value['SlowK'])
            techslowd = numtest(value['SlowD'])
            techrsi = numtest(value['RSI'])
            techfastd = numtest(value['FastD'])
            techfastk = numtest(value['FastK'])
            techwillr = numtest(value['WILLR'])
            techbband_upper = numtest(value['Real Upper Band'])
            techbband_middle = numtest(value['Real Middle Band'])
            techbband_lower = numtest(value['Real Lower Band'])
            techroc = numtest(value['ROC'])
            techrocr = numtest(value['ROCR'])

            try:
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
                        '{techdate}',
                        {techsma},
                        {techema},
                        {techmacd},
                        {techmacd_signal},
                        {techmacd_hist},
                        {techslowd},
                        {techslowk},
                        {techrsi},
                        {techfastk},
                        {techfastd},
                        {techwillr},
                        {techroc},
                        {techrocr},
                        {techbband_lower},
                        {techbband_upper},
                        {techbband_middle});
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
            technical(uuid, symbol)

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
            technical(uuid, symbol)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    dw.close()
