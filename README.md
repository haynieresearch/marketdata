# ETL Stock Data
This program is designed to extract data from a stock market API (currently [AlphaVantage](http://www.alphavantage.co)) and store it into a MySQL database.

Requirements:
* A MySQL/MariaDB server with proper access rights. Currently, we are using Amazon AWS RDS.
* An AlphaVantage API key. Depending on your use, you will need the premium data access due to the high volume of API calls.
* Python 3.5+
* Comfortable with terminal environments, this is intended to be an automated tool.

This project is still in the early development phase and we will update this document accordingly as required.

You will need to rename example.settings.yaml to settings.yaml and update with your credentials.

Note: This is intended to run daily/weekly/monthly after market close as soon as end of day data is available. You can also modify timedelta(days = 0) to -1 to run the next day on a lag or to make up missed dates.

## LICENSE
Copyright (c) 2020 Haynie IPHC, LLC\
Developed by Haynie Research & Development LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.