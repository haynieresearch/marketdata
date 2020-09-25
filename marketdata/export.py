#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-27
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		EXPORT.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-08-27 - LHAYNIE - INITIAL VERSION
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
import csv
import sys
import pandas as pd
from pathlib import Path
from .database import dw_engine

def exportcsv(table,location):

    sql = f"SELECT * from {table}"
    outFile = f"{location}{table}.csv"

    try:
        df = pd.read_sql_query(sql, dw_engine)
        df.to_csv(f"{outFile}", index=False)
    except Exception as e:
        print('Error: {}'.format(str(e)))
        dw.close()
        sys.exit(1)
