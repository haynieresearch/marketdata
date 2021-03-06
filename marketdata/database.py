#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		DATABASE.PY
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
import pymysql
from sqlalchemy import create_engine
from .settings import settings_data

db_info = {}
db_info['user'] = settings_data['databases']['marketdata']['user']
db_info['password'] = settings_data['databases']['marketdata']['password']
db_info['host'] = settings_data['databases']['marketdata']['host']
db_info['schema'] = settings_data['databases']['marketdata']['schema']

dw_info = {}
dw_info['user'] = settings_data['databases']['marketdw']['user']
dw_info['password'] = settings_data['databases']['marketdw']['password']
dw_info['host'] = settings_data['databases']['marketdw']['host']
dw_info['schema'] = settings_data['databases']['marketdw']['schema']

db = pymysql.connect(host=db_info['host'],
                     user=db_info['user'],
                     password=db_info['password'],
                     database=db_info['schema'])

dw = pymysql.connect(host=dw_info['host'],
                     user=dw_info['user'],
                     password=dw_info['password'],
                     database=dw_info['schema'])

dw_engine = create_engine(f"mysql+pymysql://{dw_info['user']}:{dw_info['password']}@{dw_info['host']}:3306/{dw_info['schema']}",connect_args={'connect_timeout': 300})
