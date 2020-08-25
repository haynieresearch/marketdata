#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-20
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		OVERVIEW.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-08-20 - LHAYNIE - INITIAL VERSION
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
import urllib.request as urlreq
import json
from re import search
from .settings import settings_data
from .database import db
from .functions

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def update_overview(uuid,symbol,date):
    cursor = db.cursor()
    try:
        cursor.execute(f"select security_id from overview where security_id = {uuid}")
        response = cursor.fetchone()

        api_function = "OVERVIEW"
        api = api_base + api_function + "&symbol=" + symbol + "&apikey=" + api_key

        try:
            data = json.loads(urlreq.urlopen(api).read().decode())
            if len(data)==0:
                print("Error updating " + symbol + ", API response empty.")
                return
            if search("Invalid API call", json.dumps(data)):
                print("Error updating " + symbol + ", API responded with error.")
                return
        except Exception as e:
            print('Error: {}'.format(str(e)))

        name = data['Name'].replace(',', '')
        country = data['Country']
        sector = data['Sector']
        industry = data['Industry']
        address = data['Address'].replace(',', '')
        fte = functions.numtest(data['FullTimeEmployees'])
        fiscal_ye = functions.numtest(data['FiscalYearEnd'])
        latest_qtr = data['LatestQuarter'] + " 00:00:00"
        if data['LatestQuarter'] == "None": latest_qtr = "0000-00-00 00:00:00"
        market_cap = functions.numtest(data['MarketCapitalization'])
        ebitda = functions.numtest(data['EBITDA'])
        pe_ratio = functions.numtest(data['PERatio'])
        peg_ratio = functions.numtest(data['PEGRatio'])
        book_value = functions.numtest(data['BookValue'])
        div_per_share = functions.numtest(data['DividendPerShare'])
        div_yield = functions.numtest(data['DividendYield'])
        eps = functions.numtest(data['EPS'])
        revenue_per_share = functions.numtest(data['RevenuePerShareTTM'])
        profit_margin = functions.numtest(data['ProfitMargin'])
        ops_margin = functions.numtest(data['OperatingMarginTTM'])
        return_on_assets = functions.numtest(data['ReturnOnAssetsTTM'])
        return_on_equity = functions.numtest(data['ReturnOnEquityTTM'])
        revenue = functions.numtest(data['RevenueTTM'])
        gross_profit = functions.numtest(data['GrossProfitTTM'])
        diluted_eps = functions.numtest(data['DilutedEPSTTM'])
        qtr_earnings_growth_yoy = functions.numtest(data['QuarterlyEarningsGrowthYOY'])
        qtr_revenue_growth_yoy = functions.numtest(data['QuarterlyRevenueGrowthYOY'])
        analyst_target_price = functions.numtest(data['AnalystTargetPrice'])
        trailing_pe = functions.numtest(data['TrailingPE'])
        forward_pe = functions.numtest(data['ForwardPE'])
        price_to_sales_ratio = functions.numtest(data['PriceToSalesRatioTTM'])
        price_to_book_ratio = functions.numtest(data['PriceToBookRatio'])
        ev_to_revenue = functions.numtest(data['EVToRevenue'])
        ev_to_ebitda = functions.numtest(data['EVToEBITDA'])
        beta = functions.numtest(data['Beta'])
        x52_week_high = functions.numtest(data['52WeekHigh'])
        x52_week_low = functions.numtest(data['52WeekLow'])
        x50_day_moving_avg = functions.numtest(data['50DayMovingAverage'])
        x200_day_moving_avg = functions.numtest(data['200DayMovingAverage'])
        shares_outstanding = functions.numtest(data['SharesOutstanding'])
        shares_float = functions.numtest(data['SharesFloat'])
        shares_short = functions.numtest(data['SharesShort'])
        shares_short_prior_month = functions.numtest(data['SharesShortPriorMonth'])
        short_ratio = functions.numtest(data['ShortRatio'])
        short_percent_outstanding = functions.numtest(data['ShortPercentOutstanding'])
        short_percent_float = functions.numtest(data['ShortPercentFloat'])
        percent_insider = functions.numtest(data['PercentInsiders'])
        percent_institution = functions.numtest(data['PercentInstitutions'])
        forward_annual_div_rate = functions.numtest(data['ForwardAnnualDividendRate'])
        forward_annual_div_yield = functions.numtest(data['ForwardAnnualDividendYield'])
        payout_ratio = functions.numtest(data['PayoutRatio'])
        div_date = data['DividendDate'] + " 00:00:00"
        if data['DividendDate'] == "None": div_date = "0000-00-00 00:00:00"
        ex_div_date = data['ExDividendDate'] + " 00:00:00"
        if data['ExDividendDate'] == "None": ex_div_date = "0000-00-00 00:00:00"
        last_split_factor = data['LastSplitFactor']
        last_split_date = data['LastSplitDate'] + " 00:00:00"
        if data['LastSplitDate'] == "None": last_split_date = "0000-00-00 00:00:00"

        if response == None:
            sql = f"""
                INSERT INTO
                overview (
                    security_id,
                    name,
                    country,
                    sector,
                    industry,
                    address,
                    fte,
                    fiscal_ye,
                    latest_qtr,
                    market_cap,
                    ebitda,
                    pe_ratio,
                    peg_ratio,
                    book_value,
                    div_per_share,
                    div_yield,
                    eps,
                    revenue_per_share,
                    profit_margin,
                    ops_margin,
                    return_on_assets,
                    return_on_equity,
                    revenue,
                    gross_profit,
                    diluted_eps,
                    qtr_earnings_growth_yoy,
                    qtr_revenue_growth_yoy,
                    analyst_target_price,
                    trailing_pe,
                    forward_pe,
                    price_to_sales_ratio,
                    price_to_book_ratio,
                    ev_to_revenue,
                    ev_to_ebitda,
                    beta,
                    52_week_high,
                    52_week_low,
                    50_day_moving_avg,
                    200_day_moving_avg,
                    shares_outstanding,
                    shares_float,
                    shares_short,
                    shares_short_prior_month,
                    short_ratio,
                    short_percent_outstanding,
                    short_percent_float,
                    percent_insider,
                    percent_institution,
                    forward_annual_div_rate,
                    forward_annual_div_yield,
                    payout_ratio,
                    div_date,
                    ex_div_date,
                    last_split_factor,
                    last_split_date)
                values(
                    {uuid},
                    '{name}',
                    '{country}',
                    '{sector}',
                    '{industry}',
                    '{address}',
                    {fte},
                    '{fiscal_ye}',
                    '{latest_qtr}',
                    {market_cap},
                    {ebitda},
                    {pe_ratio},
                    {peg_ratio},
                    {book_value},
                    {div_per_share},
                    {div_yield},
                    {eps},
                    {revenue_per_share},
                    {profit_margin},
                    {ops_margin},
                    {return_on_assets},
                    {return_on_equity},
                    {revenue},
                    {gross_profit},
                    {diluted_eps},
                    {qtr_earnings_growth_yoy},
                    {qtr_revenue_growth_yoy},
                    {analyst_target_price},
                    {trailing_pe},
                    {forward_pe},
                    {price_to_sales_ratio},
                    {price_to_book_ratio},
                    {ev_to_revenue},
                    {ev_to_ebitda},
                    {beta},
                    {x52_week_high},
                    {x52_week_low},
                    {x50_day_moving_avg},
                    {x200_day_moving_avg},
                    {shares_outstanding},
                    {shares_float},
                    {shares_short},
                    {shares_short_prior_month},
                    {short_ratio},
                    {short_percent_outstanding},
                    {short_percent_float},
                    {percent_insider},
                    {percent_institution},
                    {forward_annual_div_rate},
                    {forward_annual_div_yield},
                    {payout_ratio},
                    '{div_date}',
                    '{ex_div_date}',
                    '{last_split_factor}',
                    '{last_split_date}');
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Adding " + symbol + " to database.")
            except Exception as e:
                print('Error: {}'.format(str(e)))
        else:
            sql = f"""
                UPDATE overview SET name = '{name}',
                country = '{country}',
                sector = '{sector}',
                industry = '{industry}',
                address = '{address}',
                fte = {fte},
                fiscal_ye = '{fiscal_ye}',
                latest_qtr = '{latest_qtr}',
                market_cap = {market_cap},
                ebitda = {ebitda},
                pe_ratio = {pe_ratio},
                peg_ratio = {peg_ratio},
                book_value = {book_value},
                div_per_share = {div_per_share},
                div_yield = {div_yield},
                eps = {eps},
                revenue_per_share = {revenue_per_share},
                profit_margin = {profit_margin},
                ops_margin = {ops_margin},
                return_on_assets = {return_on_assets},
                return_on_equity = {return_on_equity},
                revenue = {revenue},
                gross_profit = {gross_profit},
                diluted_eps = {diluted_eps},
                qtr_earnings_growth_yoy = {qtr_earnings_growth_yoy},
                qtr_revenue_growth_yoy = {qtr_revenue_growth_yoy},
                analyst_target_price = {analyst_target_price},
                trailing_pe = {trailing_pe},
                forward_pe = {forward_pe},
                price_to_sales_ratio = {price_to_sales_ratio},
                price_to_book_ratio = {price_to_book_ratio},
                ev_to_revenue = {ev_to_revenue},
                ev_to_ebitda = {ev_to_ebitda},
                beta = {beta},
                52_week_high = {x52_week_high},
                52_week_low = {x52_week_low},
                50_day_moving_avg = {x50_day_moving_avg},
                200_day_moving_avg = {x200_day_moving_avg},
                shares_outstanding = {shares_outstanding},
                shares_float = {shares_float},
                shares_short = {shares_short},
                shares_short_prior_month = {shares_short_prior_month},
                short_ratio = {short_ratio},
                short_percent_outstanding = {short_percent_outstanding},
                short_percent_float = {short_percent_float},
                percent_insider = {percent_insider},
                percent_institution = {percent_institution},
                forward_annual_div_rate = {forward_annual_div_rate},
                forward_annual_div_yield = {forward_annual_div_yield},
                payout_ratio = {payout_ratio},
                div_date = '{div_date}',
                ex_div_date = '{ex_div_date}',
                last_split_factor = '{last_split_factor}',
                last_split_date = '{last_split_date}'
                WHERE security_id = {uuid};
                """
            try:
                cursor.execute(sql)
                db.commit()
                print("Updating " + symbol + " in database.")
            except Exception as e:
                print('Error: {}'.format(str(e)))
    except Exception as e:
        print(e)

def update(date):
    print("Updating Overview Data")
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_overview(uuid, symbol, date)
            #time.sleep(1)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()

def update_segment(segment,date):
    print("Updating Overview Data")
    cursor = db.cursor()
    try:
        cursor.execute(f"select uuid, symbol from security_segment where segment = '{segment}'")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_overview(uuid, symbol, date)
            #time.sleep(1)

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    db.close()
