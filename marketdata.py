#!/usr/local/bin/python3.9
#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		MARKETDATA.PY
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

if len(sys.argv) == 1:
    args = sys.argv
    print("No option provided, use --help for options.")
    exit(0)
elif len(sys.argv) == 2:
    args = sys.argv
    arg1 = sys.argv[1]
elif len(sys.argv) == 3:
    args = sys.argv
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
elif len(sys.argv) == 4:
    args = sys.argv
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
else:
    print("No option provided, use --help for options.")
    exit(0)

if len(args) > 1:
    if arg1.lower() == "--help":
        print("help stuff")

    elif arg1.lower() == "--exchange":
        if arg2.lower() == "other":
            import marketdata.symbol
            marketdata.symbol.update(marketdata.symbol.other(),1)
        elif arg2.lower() == "nasdaq":
            import marketdata.symbol
            marketdata.symbol.update(marketdata.symbol.nasdaq(),2)
        else:
            print("Error: unrecognized exchange code.")

    elif arg1.lower() == "--daily":
        if len(sys.argv) == 2:
            import marketdata.daily
            marketdata.daily.update()
        else:
            print("Error: other error.")

    elif arg1.lower() == "--news":
        if len(sys.argv) == 2:
            import marketdata.news
            marketdata.news.update()
        else:
            print("Error: other error.")

    elif arg1.lower() == "--history":
        if len(sys.argv) == 2:
            print("Error: you must specify a date.")
            exit(0)
        else:
            import marketdata.history
            marketdata.history.update(arg2.lower())

    elif arg1.lower() == "--export":
        if len(sys.argv) == 2:
            print("Error: you must specify which table to export.")
            exit(0)
        elif len(sys.argv) == 3:
            print("Error: you must specify an output folder.")
            exit(0)
        else:
            import marketdata.export
            marketdata.export.exportcsv(arg2.lower(),arg3.lower())

    elif arg1.lower() == "--check_config":
        print("Just making sure everything works!")

    else:
        print("Error: invalid option, use --help for options.")
else:
    print("No option provided, use --help for options.")
exit(0)
