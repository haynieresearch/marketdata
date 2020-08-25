#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-25
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		CSV2MYSQL.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-08-25 - LHAYNIE - INITIAL VERSION
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
from .settings import settings_data
from .database import db
import pandas as pd
import sys

def csv2mysql(file,table):
    sql = f"LOAD DATA LOCAL INFILE '{file}' INTO TABLE {table}\
     FIELDS TERMINATED BY ',' ENCLOSED BY '"' IGNORE 1 LINES;"

    try:
        cursor = db.cursor()
        cursor.execute(sql)
        print('Succuessfully loaded the table from input file.')
        db.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
