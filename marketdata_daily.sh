#!/bin/bash
python_location=/usr/bin/
python_bin=python3.6
python=$python_location$python_bin

ps_bin=/usr/bin/ps
grep_bin=/usr/bin/grep
wc_bin=/usr/bin/wc
sleep_bin=/bin/sleep
mail_bin=/usr/bin/mail

location=/path/to/marketdata/script
email=user@domain.tld

start=`date +%s`

cd $location

$python_bin $location/marketdata.py --exchange other > /dev/null 2>&1 &
$python_bin $location/marketdata.py --exchange nasdaq > /dev/null 2>&1 &

while [ $($ps_bin -f -C $python_bin | $grep_bin marketdata.py | $wc_bin -l) -ge 1 ]; do
        $sleep_bin 300
done

$python_bin $location/marketdata.py --daily --segment a > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment b > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment c > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment d > /dev/null 2>&1 &

while [ $($ps_bin -f -C $python_bin | $grep_bin marketdata.py | $wc_bin -l) -ge 1 ]; do
        $sleep_bin 300
done

$python_bin $location/marketdata.py --daily --segment e > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment f > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment g > /dev/null 2>&1 &
$python_bin $location/marketdata.py --daily --segment h > /dev/null 2>&1 &

while [ $($ps_bin -f -C $python_bin | $grep_bin marketdata.py | $wc_bin -l) -ge 1 ]; do
        $sleep_bin 300
done

$python_bin $location/marketdata.py --technical --segment a > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment b > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment c > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment d > /dev/null 2>&1 &

while [ $($ps_bin -f -C $python_bin | $grep_bin marketdata.py | $wc_bin -l) -ge 1 ]; do
        $sleep_bin 300
done

$python_bin $location/marketdata.py --technical --segment e > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment f > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment g > /dev/null 2>&1 &
$python_bin $location/marketdata.py --technical --segment h > /dev/null 2>&1 &

while [ $($ps_bin -f -C $python_bin | $grep_bin marketdata.py | $wc_bin -l) -ge 1 ]; do
        $sleep_bin 300
done

$python_bin $location/marketdata.py --overview > /dev/null 2>&1

end=`date +%s`

runtime="Daily MarketData Process Completed. Total runtime: $((($(date +%s)-$start)/60)) minutes."
$mail_bin -s 'Daily MarketData Process' $email <<< $runtime
exit 0
