#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		FUNCTIONS.PY
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

def numtest(var_input):
    if isinstance(input, float) == True:
        var_input = var_input
    elif isinstance(input, int) == True:
        var_input = float(var_input)
    elif isinstance(input, str) == True:
        var_input = float(var_input)
    elif var_input == None:
        var_input = float(0)
    else:
        var_input = float(var_input)
    return var_input
