#!/bin/bash
start=`date +%s`

env=prod
dir=/path/to/$env/jobs
mdir=/path/to/$env/models
job_spawn="/usr/bin/python3.6 /path/to/job_spawner/job.py"
sas="/path/to/sas -noterminal"
log="/tmp/marketdata_daily_$$"

cd /path/to/marketdata

echo "Updating Symbol List" >> "$log"
/usr/bin/python3.6 /path/to/marketdata/marketdata.py --exchange other &
/usr/bin/python3.6 /path/to/marketdata/marketdata.py --exchange nasdaq &

while [ $(/usr/bin/ps -f -C python3.6 | grep marketdata.py | wc -l) -ge 1 ]; do
        echo "Waiting on symbol list process to finish..." >> "$log"
	sleep 60
done

echo "Updating Daily Data" >> "$log"
/usr/bin/python3.6 /path/to/marketdata/marketdata.py --daily &

while [ $(/usr/bin/ps -f -C python3.6 | grep marketdata.py | wc -l) -ge 1 ]; do
        "Waiting on daily data process to finish..." >> "$log"
	sleep 60
done

echo "Updating Overview Data" >> "$log"
/usr/bin/python3.6 /path/to/marketdata/marketdata.py --overview

$job_spawn "$sas $dir/market_data_import.sas" 3 >> "$log"

end=`date +%s`
runtime="Some Title Goes Here
Daily Production Jobs Completed
Total runtime: $((($(date +%s)-$start)/60)) minutes

Log contents:
"
/usr/bin/mail -s 'Daily Production Jobs' your.email@someplace.com <<< $runtime$(cat $log)
rm "$log"
exit 0
