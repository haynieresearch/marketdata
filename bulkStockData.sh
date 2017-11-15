#!/bin/bash
clear
source keys.cfg

outfile="HRD.STOCKS.HISTORY"

in=$(mktemp)
out=$(mktemp)
tmpnasdaq=$(mktemp)
tmpnyse=$(mktemp)
nasdaq=$(mktemp)
nyse=$(mktemp)
history=$(mktemp)

awk="/usr/bin/awk"
wget="/usr/bin/wget"
sed="/bin/sed"
wc="/usr/bin/wc"

$wget -O $tmpnasdaq "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download" >/dev/null 2>&1
$wget -O $tmpnyse "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download" >/dev/null 2>&1

sed -i -e 's/"//g' $tmpnasdaq
sed -i -e 's/"//g' $tmpnyse

echo "Building symbol list for processing..."
$awk -F, '{printf("%-5s\n", $1)}' $tmpnasdaq > $nasdaq
$awk -F, '{printf("%-5s\n", $1)}' $tmpnyse > $nyse

rm ${tmpnasdaq}
rm ${tmpnyse}

nasdaqCount=$($wc -l < $nasdaq)
nyseCount=$($wc -l < $nyse)

echo "Total NASDAQ Symbols: " $nasdaqCount
echo "Total NYSE Symbols: " $nyseCount

function getStockData
  {
    $wget -O $in "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol="$1"&apikey="$apikey"&datatype=csv" >/dev/null 2>&1
    $sed -i -e 's/-/,/g' $in
    $sed -i 1d $in
    while read line
    do
        echo "$1,$line" >> $out
    done < $in
    $awk -F, '{printf("%-5s%4s%2s%2s%010.4f%010.4f%010.4f%010.4f%010d\n", $1, $2, $3, $4, $5, $6, $7, $8, $9)}' $out >> $outfile
    $sed -i -e '/Invalid API call/d' $outfile
    $sed -i -e '/Error Message/d' $outfile
    rm ${in}
    rm ${out}
  }

while read symbol
  do
    echo "Processing " $symbol
    getStockData $symbol
  done < $nasdaq

rm ${nasdaq}

while read symbol
  do
    echo "Processing " $symbol
    getStockData $symbol
  done < $nyse
rm ${nyse}
