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
import urllib.request as urlreq
import json
from re import search
from datetime import date, datetime, timedelta
from .settings import *
from .database import *

now = datetime.strftime(datetime.utcnow(),"%H:%M:%S")
t1 = "20:00:00"
t2 = "23:59:59"

if now >= t1 and now <= t2:
    today = date.today() - timedelta(days = 0)
else:
    today = date.today() - timedelta(days = -1)

data_date = today.strftime("%Y-%m-%d")
sql_date = data_date + " 00:00:00"

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def update_technical(uuid,symbol):
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from technical where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        sma_api = api_base + "SMA" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        ema_api = api_base + "EMA" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        macd_api = api_base + "MACD" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        stoch_api = api_base + "STOCH" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        rsi_api = api_base + "RSI" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        stochrsi_api = api_base + "STOCHRSI" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        willr_api = api_base + "WILLR" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        bbands_api = api_base + "BBANDS" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        roc_api = api_base + "ROC" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key
        rocr_api = api_base + "ROCR" + "&symbol=" + symbol + "&interval=daily&time_period=10&series_type=open&apikey=" + api_key

        try:
            sma_data = json.loads(urlreq.urlopen(sma_api).read().decode())
            if len(sma_data)==0:
                print("Error updating SMA " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(sma_api)):
                print("Error updating SMA " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            ema_data = json.loads(urlreq.urlopen(ema_api).read().decode())
            if len(ema_data)==0:
                print("Error updating EMA " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(ema_data)):
                print("Error updating EMA " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            macd_data = json.loads(urlreq.urlopen(macd_api).read().decode())
            if len(macd_data)==0:
                print("Error updating MACD " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(macd_data)):
                print("Error updating MACD " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            stoch_data = json.loads(urlreq.urlopen(stoch_api).read().decode())
            if len(stoch_data)==0:
                print("Error updating STOCH " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(stoch_data)):
                print("Error updating STOCH " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            rsi_data = json.loads(urlreq.urlopen(rsi_api).read().decode())
            if len(rsi_data)==0:
                print("Error updating RSI " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(rsi_data)):
                print("Error updating RSI " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            stochrsi_data = json.loads(urlreq.urlopen(stochrsi_api).read().decode())
            if len(stochrsi_data)==0:
                print("Error updating STOCH RSI " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(stochrsi_data)):
                print("Error updating STOCH RSI " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            willr_data = json.loads(urlreq.urlopen(willr_api).read().decode())
            if len(willr_data)==0:
                print("Error updating WILL R " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(willr_data)):
                print("Error updating WILL R " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            bbands_data = json.loads(urlreq.urlopen(bbands_api).read().decode())
            if len(bbands_data)==0:
                print("Error updating B BANDS " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(bbands_data)):
                print("Error updating B BANDS " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            roc_data = json.loads(urlreq.urlopen(roc_api).read().decode())
            if len(roc_data)==0:
                print("Error updating ROC " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(roc_data)):
                print("Error updating ROC  " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        try:
            rocr_data = json.loads(urlreq.urlopen(rocr_api).read().decode())
            if len(rocr_data)==0:
                print("Error updating ROC R " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(rocr_data)):
                print("Error updating ROC R " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print(e)

        sma_data_response = sma_data[[i for i in sma_data.keys() if 'Technical Analysis' in i][0]]
        if list(sma_data_response.keys())[0] != data_date:
            print("Error updating SMA for " + symbol + ", API responded with incorrect date.")
            return

        ema_data_response = ema_data[[i for i in ema_data.keys() if 'Technical Analysis' in i][0]]
        if list(ema_data_response.keys())[0] != data_date:
            print("Error updating EMA for " + symbol + ", API responded with incorrect date.")
            return

        macd_data_response = macd_data[[i for i in macd_data.keys() if 'Technical Analysis' in i][0]]
        if list(macd_data_response.keys())[0] != data_date:
            print("Error updating MACD for " + symbol + ", API responded with incorrect date.")
            return

        stoch_data_response = stoch_data[[i for i in stoch_data.keys() if 'Technical Analysis' in i][0]]
        if list(stoch_data_response.keys())[0] != data_date:
            print("Error updating STOCH for " + symbol + ", API responded with incorrect date.")
            return

        rsi_data_response = rsi_data[[i for i in rsi_data.keys() if 'Technical Analysis' in i][0]]
        if list(rsi_data_response.keys())[0] != data_date:
            print("Error updating RSI for " + symbol + ", API responded with incorrect date.")
            return

        stochrsi_data_response = stochrsi_data[[i for i in stochrsi_data.keys() if 'Technical Analysis' in i][0]]
        if list(stochrsi_data_response.keys())[0] != data_date:
            print("Error updating STOCH RSI for " + symbol + ", API responded with incorrect date.")
            return

        willr_data_response = willr_data[[i for i in willr_data.keys() if 'Technical Analysis' in i][0]]
        if list(willr_data_response.keys())[0] != data_date:
            print("Error updating WILL R for " + symbol + ", API responded with incorrect date.")
            return

        bbands_data_response = bbands_data[[i for i in bbands_data.keys() if 'Technical Analysis' in i][0]]
        if list(bbands_data_response.keys())[0] != data_date:
            print("Error updating B BANDS for " + symbol + ", API responded with incorrect date.")
            return

        roc_data_response = roc_data[[i for i in roc_data.keys() if 'Technical Analysis' in i][0]]
        if list(roc_data_response.keys())[0] != data_date:
            print("Error updating ROC for " + symbol + ", API responded with incorrect date.")
            return

        rocr_data_response = rocr_data[[i for i in rocr_data.keys() if 'Technical Analysis' in i][0]]
        if list(rocr_data_response.keys())[0] != data_date:
            print("Error updating ROC R for " + symbol + ", API responded with incorrect date.")
            return

        sma = sma_data_response[data_date]['SMA']
        ema = ema_data_response[data_date]['EMA']
        macd = macd_data_response[data_date]['MACD']
        macd_hist = macd_data_response[data_date]['MACD_Hist']
        macd_signal = macd_data_response[data_date]['MACD_Signal']
        stoch_slowk = stoch_data_response[data_date]['SlowK']
        stoch_slowd = stoch_data_response[data_date]['SlowD']
        rsi = rsi_data_response[data_date]['RSI']
        stochrsi_fastk = stochrsi_data_response[data_date]['FastK']
        stochrsi_fastd = stochrsi_data_response[data_date]['FastD']
        willr = willr_data_response[data_date]['WILLR']
        bbands_upper = bbands_data_response[data_date]['Real Upper Band']
        bbands_lower = bbands_data_response[data_date]['Real Lower Band']
        bbands_middle = bbands_data_response[data_date]['Real Middle Band']
        roc = roc_data_response[data_date]['ROC']
        rocr = rocr_data_response[data_date]['ROCR']

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
            update_technical(uuid, symbol)

    except Exception as e:
        print(e)
    db.close()
