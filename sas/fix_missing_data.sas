/**********************************************************
#* CATEGORY	SAS
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* FILE		fix_missing_data.sas
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

proc sql;
	create table record_count as
		select daily_price_data.date,
		count(security_uuid) as records
		from daily_price_data
		group by daily_price_data.date
		order by date desc;
quit;

proc sql;
	select avg(record_count.records) into:average_records
	from work.record_count record_count
	where date >= today()-7;
quit;

proc sql;
	select cats("[", date ,"]") into:date_list separated by ' '
	from record_count
	where records < (&average_records.*0.9) and date >= today()-1800;
run;

%macro fix_history(dates);
	%let count=%sysfunc(countw(&dates));

	%do i=1 %to &count;
		%let date = %sysfunc(putn(%sysfunc(compress(%scan(&dates, &i), '[]')),yymmddd10.));
		x "cd /path/to/marketdata; /usr/bin/python3.6 /path/to/marketdata/marketdata.py --history &date.";
	%end;
%mend;

%fix_history(&date_list);

proc datasets library=work kill nolist; quit;
%post_process;
