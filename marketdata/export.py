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
from pathlib import Path
from .database import db

def exportcsv(table,location):

    sql = f"SELECT * from {table}"
    outFile = f"{location}{table}.csv"

    cursor = db.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
    except Exception as e:
        print('Error: {}'.format(str(e)))
        db.close()

    if rows:
        Path(f"{outFile}").touch()
        columns = [i[0] for i in cursor.description]
        fp = open(outFile, 'w')
        csvFile = csv.writer(fp, lineterminator = '\n')
        csvFile.writerow(columns)
        csvFile.writerows(rows)
        fp.close()
    else:
        sys.exit(f"Table {table} returned zero observations.")
