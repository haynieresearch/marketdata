/**********************************************************
#* CATEGORY	SAS
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		market_data_import.sas
#**********************************************************
#Copyright 2020 Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a acopy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.*/

libname out '/path/to/save/datasets/';

options mprint symbolgen;
%macro export(table);
	x "rm /path/to/marketdata/datasets/&table..csv || True";
	x "mysql --defaults-extra-file=/path/to/mysqlconf/mysql.conf -e 'select * from marketdata.&table.' | sed  's/\t/,/g' > /path/to/marketdata/datasets/&table..csv";
%mend export;

%export(currency);
%export(exchange);
%export(security);
%export(type);
%export(overview);
%export(daily);

data out.currency;
    infile "/path/to/marketdata/datasets/currency.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    input 	uuid
    	  	currency $;

    format 	uuid 10.
    		currency $3.;
run;

data out.exchange;
    infile "/path/to/marketdata/datasets/exchange.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    input uuid
    	  exchange $;

    format uuid 10.
    	   exchange $10.;
run;

data out.security;
	infile "/path/to/marketdata/datasets/security.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    input uuid
    	  symbol $
    	  type_id
    	  exchange_id
    	  currency_id;

    format uuid 10.
    	   symbol $10.
    	   type_id 10.
    	   exchange_id 10.
    	   currency_id 10.;
run;

data out.type;
    infile "/path/to/marketdata/datasets/type.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    length uuid 8 type $12;

    input uuid
    	  type $;

    format uuid 10.
    	   type $12.;
run;

data out.overview;
    infile "/path/to/marketdata/datasets/overview.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    length uuid 8
    	   security_id 8
    	   name $150
    	   country $150
    	   sector $150
    	   industry $150
    	   address $150
    	   fte $10
    	   fiscal_ye $10
    	   latest_qtr $10
    	   market_cap $15
    	   ebitda 8
    	   pe_ratio 8
    	   peg_ratio 8
    	   book_value 8
    	   div_per_share 8
    	   div_yield 8
    	   eps 8
    	   revenue_per_share 8
    	   profit_margin 8
    	   ops_margin 8
    	   return_on_assets 8
    	   return_on_equity 8
    	   revenue 8
    	   gross_profit 8
    	   diluted_eps 8
    	   qtr_earnings_growth_yoy 8
    	   qtr_revenue_growth_yoy 8
    	   analyst_target_price 8
    	   trailing_pe 8
    	   forward_pe 8
    	   price_to_sales_ratio 8
    	   price_to_book_ratio 8
    	   ev_to_revenue 8
    	   ev_to_ebitda 8
    	   beta 8
    	   _52_week_high 8
    	   _52_week_low 8
    	   _50_day_moving_avg 8
    	   _200_day_moving_avg 8
    	   shares_outstanding 8
    	   shares_float 8
    	   shares_short 8
    	   shares_short_prior_month 8
    	   short_ratio 8
    	   short_percent_outstanding 8
    	   short_percent_float 8
    	   percent_insider 8
    	   percent_institution 8
    	   forward_annual_div_rate 8
    	   forward_annual_div_yield 8
    	   payout_ratio 8
    	   div_date $10
    	   ex_div_date $10
    	   last_split_factor $20
    	   last_split_date $10;

    input uuid
    	  security_id
    	  name $
    	  country $
    	  sector $
    	  industry $
    	  address $
    	  fte $
    	  fiscal_ye $
    	  latest_qtr $
    	  market_cap $
    	  ebitda
    	  pe_ratio
    	  peg_ratio
    	  book_value
    	  div_per_share
    	  div_yield
    	  eps
    	  revenue_per_share
    	  profit_margin
    	  ops_margin
    	  return_on_assets
    	  return_on_equity
    	  revenue
    	  gross_profit
    	  diluted_eps
    	  qtr_earnings_growth_yoy
    	  qtr_revenue_growth_yoy
    	  analyst_target_price
    	  trailing_pe
    	  forward_pe
    	  price_to_sales_ratio
    	  price_to_book_ratio
    	  ev_to_revenue
    	  ev_to_ebitda
    	  beta
    	  _52_week_high
    	  _52_week_low
    	  _50_day_moving_avg
    	  _200_day_moving_avg
    	  shares_outstanding
    	  shares_float
    	  shares_short
    	  shares_short_prior_month
    	  short_ratio
    	  short_percent_outstanding
    	  short_percent_float
    	  percent_insider
    	  percent_institution
    	  forward_annual_div_rate
    	  forward_annual_div_yield
    	  payout_ratio
    	  div_date $
    	  ex_div_date $
    	  last_split_factor $
    	  last_split_date $;

    format uuid 10.
    	   security_id 10.
    	   name $150.
    	   country $150.
    	   sector $150.
    	   industry $150.
    	   address $150.
    	   fte $10.
    	   fiscal_ye $10.
    	   latest_qtr $10.
    	   market_cap $15.
    	   ebitda 15.
    	   pe_ratio 15.
    	   peg_ratio 15.
    	   book_value 15.
    	   div_per_share 15.
    	   div_yield 15.
    	   eps 15.
    	   revenue_per_share 15.
    	   profit_margin 15.
    	   ops_margin 15.
    	   return_on_assets 15.
    	   return_on_equity 15.
    	   revenue 15.
    	   gross_profit 15.
    	   diluted_eps 15.
    	   qtr_earnings_growth_yoy 15.
    	   qtr_revenue_growth_yoy 15.
    	   analyst_target_price 15.
    	   trailing_pe 15.
    	   forward_pe 15.
    	   price_to_sales_ratio 15.
    	   price_to_book_ratio 15.
    	   ev_to_revenue 15.
    	   ev_to_ebitda 15.
    	   beta 15.
    	   _52_week_high 15.
    	   _52_week_low 15.
    	   _50_day_moving_avg 15.
    	   _200_day_moving_avg 15.
    	   shares_outstanding 15.
    	   shares_float 15.
    	   shares_short 15.
    	   shares_short_prior_month 15.
    	   short_ratio 15.
    	   short_percent_outstanding 15.
    	   short_percent_float 15.
    	   percent_insider 15.
    	   percent_institution 15.
    	   forward_annual_div_rate 15.
    	   forward_annual_div_yield 15.
    	   payout_ratio 15.
    	   div_date $10.
    	   ex_div_date $10.
    	   last_split_factor $10.
    	   last_split_date $10.;
run;

data out.daily;
    infile "/path/to/marketdata/datasets/daily.csv"
    delimiter = ","
    missover dsd
    firstobs=2
    lrecl=32767;

    length uuid 8
    	   security_id 8
    	   date $10
    	   open 8
    	   high 8
    	   low 8
    	   close 8
    	   volume 8
    	   unadjusted_open 8
    	   unadjusted_high 8
    	   unadjusted_low 8
    	   unadjusted_close 8
    	   unadjusted_volume 8
    	   adjusted_open 8
    	   adjusted_high 8
    	   adjusted_low 8
    	   adjusted_close 8
    	   adjusted_volume 8
    	   change 8
    	   change_percent 8;

    input uuid
    	  security_id
    	  date $
    	  open
    	  high
    	  low
    	  close
    	  volume
    	  unadjusted_open
    	  unadjusted_high
    	  unadjusted_low
    	  unadjusted_close
    	  unadjusted_volume
    	  adjusted_open
    	  adjusted_high
    	  adjusted_low
    	  adjusted_close
    	  adjusted_volume
    	  change
    	  change_percent;

    format uuid 20.
    	   security_id 10.
    	   date $10.
    	   open 15.
    	   high 15.
    	   low 15.
    	   close 15.
    	   volume 15.
    	   unadjusted_open 15.
    	   unadjusted_high 15.
    	   unadjusted_low 15.
    	   unadjusted_close 15.
    	   unadjusted_volume 15.
    	   adjusted_open 15.
    	   adjusted_high 15.
    	   adjusted_low 15.
    	   adjusted_close 15.
    	   adjusted_volume 15.
    	   change 15.
    	   change_percent 15.;
run;

proc datasets library=work kill nolist; quit;
