#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		EXPORT.PY
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
from .settings import settings_data
from .database import dw

def exportcsv(table,location):
    outFile = f"{location}{table}.csv"
    chunk_size = settings_data['databases']['marketdw']['chunk_size']
    dw_cursor = dw.cursor()

    dw_cursor.execute(f"SELECT COUNT(*) FROM {table}")
    row_count = dw_cursor.fetchone()[0]

    dw_cursor.execute(f"SELECT * FROM {table} limit 1")
    with open(outFile, 'w', newline='') as outCsv:
        wr = csv.writer(outCsv)
        wr.writerow([d[0] for d in dw_cursor.description])

    try:
        for offset in range(0, row_count, chunk_size):
            dw_cursor.execute(f"SELECT * FROM {table} LIMIT {chunk_size} OFFSET {offset};")

            with open(outFile, 'a', newline='') as outCsv:
                csvwriter = csv.writer(outCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in dw_cursor:
                    csvwriter.writerow(row)
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
