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

def tech_ind(base,sym,ind,key):
    api = f"{base}/stock/{sym}/indicator/{ind}?range=5d&token={key}"
    response_data = json.loads(urlreq.urlopen(api).read().decode())
    return response_data['indicator'][0][4]

def tech_ind_range(base,sym,ind,key):
    api = f"{base}/stock/{sym}/indicator/{ind}?range=ytd&token={key}"
    response_data = json.loads(urlreq.urlopen(api).read().decode())
    response = {}
    response[0] = response_data['indicator'][0][-1]
    response[1] = response_data['indicator'][1][-1]
    response[2] = response_data['indicator'][2][-1]
    return response

def update_technical(uuid,symbol,date):
    data_date = date
    sql_date = data_date + " 00:00:00"
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from technical where security_id = {uuid} AND date = '{sql_date}'")
        response = cursor.fetchone()

        sma             = numtest(tech_ind(api_base,symbol,"sma",api_key))
        ema             = numtest(tech_ind(api_base,symbol,"ema",api_key))
        willr           = numtest(tech_ind(api_base,symbol,"willr",api_key))
        decay           = numtest(tech_ind(api_base,symbol,"decay",api_key))
        fisher          = numtest(tech_ind(api_base,symbol,"fisher",api_key))
        kama            = numtest(tech_ind(api_base,symbol,"fisher",api_key))
        kvo             = numtest(tech_ind(api_base,symbol,"kvo",api_key))
        linreg          = numtest(tech_ind(api_base,symbol,"linreg",api_key))
        linregintercept = numtest(tech_ind(api_base,symbol,"linregintercept",api_key))
        linregslope     = numtest(tech_ind(api_base,symbol,"linregslope",api_key))
        macd            = numtest(tech_ind_range(api_base,symbol,"macd",api_key)[0])
        macd_signal     = numtest(tech_ind_range(api_base,symbol,"macd",api_key)[1])
        macd_hist       = numtest(tech_ind_range(api_base,symbol,"macd",api_key)[2])
        bbands_lower    = numtest(tech_ind_range(api_base,symbol,"bbands",api_key)[0])
        bbands_middle   = numtest(tech_ind_range(api_base,symbol,"bbands",api_key)[1])
        bbands_upper    = numtest(tech_ind_range(api_base,symbol,"bbands",api_key)[2])

        if response == None:
            sql = f"""
                INSERT INTO
                technical (
                    security_id,
                    date,
                    sma,
                    ema,
                    willr,
                    decay,
                    fisher,
                    kama,
                    kvo,
                    linreg,
                    linregintercept,
                    linregslope,
                    macd,
                    macd_signal,
                    macd_hist,
                    bbands_lower,
                    bbands_upper,
                    bbands_middle)
                values(
                    {uuid},
                    '{sql_date}',
                    {sma},
                    {ema},
                    {willr},
                    {decay},
                    {fisher},
                    {kama},
                    {kvo},
                    {linreg},
                    {linregintercept},
                    {linregslope},
                    {macd},
                    {macd_signal},
                    {macd_hist},
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
                willr = {macd},
                decay = {macd_signal},
                fisher = {macd_hist},
                kama = {stoch_slowd},
                kvo = {stoch_slowk},
                linreg = {rsi},
                linregintercept = {stochrsi_fastk},
                linregslope = {stochrsi_fastd},
                macd = {willr},
                macd_signal = {roc},
                macd_hist = {rocr},
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

def update(date):
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_technical(uuid, symbol, date)

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

    except Exception as e:
        print(e)
    db.close()
