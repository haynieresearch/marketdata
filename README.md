# Market Data [![Build Status](https://travis-ci.com/haynieresearch/marketdata.svg?branch=master)](https://travis-ci.com/haynieresearch/marketdata) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/729efafdf51b47adab28e5d5a83ae067)](https://app.codacy.com/gh/haynieresearch/stock-data?utm_source=github.com&utm_medium=referral&utm_content=haynieresearch/stock-data&utm_campaign=Badge_Grade_Dashboard)
This program is designed to extract data from a stock market API (currently [IEX](https://iexcloud.io/docs/api)) and store it into a MySQL database.

## REQUIREMENTS
* A MySQL/MariaDB master server and read replica with proper access rights. Currently, we are using Amazon AWS RDS.
* An IEX Cloud API key. Depending on your use, you will need the premium data access due to the high volume of API calls.
* Python 3.5+
* Comfortable with terminal environments, this is intended to be an automated tool.

This project is still in the early development phase and we will update this document accordingly as required.

## INSTALL
pip3 install -r requirements.txt\
rename example.settings.yaml to settings.yaml and update with your credentials\
load sql files into your MySQL database\

## SETTINGS
In the settings.yaml file you will notice two databases. The first, marketdata, is the master MariaDB server where write privileges are executed. The second, marketdw (data warehouse), is a read replica of the master MariaDB server. The purpose of this is to allow read only operations such as the export functionality to happen on the read only server vs. the master. If you do not want to setup both a master and replica database; simply put the same credentials for both marketdata and marketdw.

The datasources section for the most part you can leave as-is with the exception of adding your specific API keys.

## USAGE
marketdata.py --exchange nasdaq (update symbol list for NASDAQ)\
marketdata.py --exchange other (update symbol list for everything other than NASDAQ)\
marketdata.py --daily (update daily price data, see note below)\
marketdata.py --history YYYY-MM-DD (update historical price data)\
marketdata.py --overview (update overview/fundamental data)\
marketdata.py --export table_name /path/to/save/csv/ (export mysql table as csv)

Note: We use the "previous" API endpoint from IEX for the daily function to save on costs as the weighting for previous data weighting is two; whereas the historical endpoint is weighted as ten. However, this means you need to schedule the daily job to run automatically to download consistently. We are aware system issues happen, so there is now a history function to pull any missing data. Just realize it is quite a bit more expensive to pull this data vs. the daily data. The daily data using the "previous" API endpoint is available after 4AM ET Tues-Sat.

You may notice that the export function is technically not the most efficient. However, we ran into issues with memory usage with more traditional methods of pulling data down from a MySQL table. This method is a compromise of efficiency and best use of system resources.

## IN PROGRESS
We are switching direction with the technical indicators from pulling down from a provider to calculating in house. With almost all of the data providers it has proven to be costly both in processing time and dollars to effectively gather all of this data. As we transition from the old process to new, we will include our SAS code to calculate the technical indicators so you can replicate in your environment.

## GOAL
The goal of this project is to enable the creation of time series market datasets for statistical and quantitative analysis, as well as model development. Currently, there are many datasets that exist for historical price data (open, high, low, close), but none that include technical and fundamental data as well in the same observation.

## LICENSE
Copyright (c) 2020 Haynie IPHC, LLC\
Developed by Haynie Research & Development, LLC for Black Label Investment Partners, LLC under license.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
