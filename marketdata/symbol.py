#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-20
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		SYMBOL.PY
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
import pandas as pd
from .settings import settings_data
from .database import db

datasrc = {}
datasrc['nasdaq'] = settings_data['datasources']['SymbolList']['nasdaq']
datasrc['other'] = settings_data['datasources']['SymbolList']['other']

def nasdaq(source = datasrc['nasdaq']):
    data = pd.read_csv(source,sep="|")
    data.columns = ['symbol', 'name', 'category', 'test issue', 'status', 'lot', 'etf', 'nextshares']
    return sorted(list(data.symbol));

def other(source = datasrc['other']):
    data = pd.read_csv(source,sep="|")
    data.columns = ['symbol', 'name', 'category', 'test issue', 'status', 'lot', 'etf', 'nextshares']
    return sorted(list(data.symbol));

def update(exchange,exchange_id):
    cursor = db.cursor()
    try:
        for index in range(len(exchange)):
            try:
                cursor.execute('select symbol from security where symbol = ' + '"' + exchange[index] + '"')
            except Exception as e:
                print('Error: {}'.format(str(e)))
            response = cursor.fetchone()
            symbol = exchange[index]

            if response == None:
                sql = f"INSERT INTO security (symbol, type_id, exchange_id, currency_id) VALUES('{symbol}', 1, {exchange_id}, 1);"
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("Symbol:" + symbol + " added to database.")
                except Exception as e:
                    db.rollback()
                    print('Error: {}'.format(str(e)))
            else:
                sql = f"""
                    UPDATE security SET type_id = 1,
                    exchange_id = {exchange_id},
                    currency_id = 1
                    WHERE symbol = \"{symbol}\";
                    """
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("Updating " + symbol + " in database.")
                except Exception as e:
                    print("Error updating " + symbol)
                    print('Error: {}'.format(str(e)))
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()
