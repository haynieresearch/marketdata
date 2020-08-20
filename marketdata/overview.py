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
import os
import sys
import urllib.request as urlreq
import json
from re import search
from .settings import *
from .database import *

api_base = settings_data['datasources']['AlphaVantage']['url']
api_key = settings_data['datasources']['AlphaVantage']['key']

def update_overview(uuid,symbol):
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
            print(e)

        name = data['Name'].replace(',', '')
        country = data['Country']
        sector = data['Sector']
        industry = data['Industry']
        address = data['Address'].replace(',', '')
        fte = data['FullTimeEmployees']
        if fte == "None": fte = 0
        fiscal_ye = data['FiscalYearEnd']
        latest_qtr = data['LatestQuarter'] + " 00:00:00"
        if data['LatestQuarter'] == "None": latest_qtr = "0000-00-00 00:00:00"
        market_cap = data['MarketCapitalization']
        if market_cap == "None": market_cap = 0
        ebitda = data['EBITDA']
        if ebitda == "None": ebitda = 0
        pe_ratio = data['PERatio']
        if pe_ratio == "None": pe_ratio = 0
        peg_ratio = data['PEGRatio']
        if peg_ratio == "None": peg_ratio = 0
        book_value = data['BookValue']
        if book_value == "None": book_value = 0
        div_per_share = data['DividendPerShare']
        if div_per_share == "None": div_per_share = 0
        div_yield = data['DividendYield']
        if div_yield == "None": div_yield = 0
        eps = data['EPS']
        if eps == "None": eps = 0
        revenue_per_share = data['RevenuePerShareTTM']
        if revenue_per_share == "None": revenue_per_share = 0
        profit_margin = data['ProfitMargin']
        if profit_margin == "None": profit_margin = 0
        ops_margin = data['OperatingMarginTTM']
        if ops_margin == "None": ops_margin = 0
        return_on_assets = data['ReturnOnAssetsTTM']
        if return_on_assets == "None": return_on_assets = 0
        return_on_equity = data['ReturnOnEquityTTM']
        if return_on_equity == "None": return_on_equity = 0
        revenue = data['RevenueTTM']
        if revenue == "None": revenue = 0
        gross_profit = data['GrossProfitTTM']
        if gross_profit == "None": gross_profit = 0
        diluted_eps = data['DilutedEPSTTM']
        if diluted_eps == "None": diluted_eps = 0
        qtr_earnings_growth_yoy = data['QuarterlyEarningsGrowthYOY']
        if qtr_earnings_growth_yoy == "None": qtr_earnings_growth_yoy = 0
        qtr_revenue_growth_yoy = data['QuarterlyRevenueGrowthYOY']
        if qtr_revenue_growth_yoy == "None": qtr_revenue_growth_yoy = 0
        analyst_target_price = data['AnalystTargetPrice']
        if analyst_target_price == "None": analyst_target_price = 0
        trailing_pe = data['TrailingPE']
        if trailing_pe == "None": trailing_pe = 0
        forward_pe = data['ForwardPE']
        if forward_pe == "None": forward_pe = 0
        price_to_sales_ratio = data['PriceToSalesRatioTTM']
        if price_to_sales_ratio == "None": price_to_sales_ratio = 0
        price_to_book_ratio = data['PriceToBookRatio']
        if price_to_book_ratio == "None": price_to_book_ratio = 0
        ev_to_revenue = data['EVToRevenue']
        if ev_to_revenue == "None": ev_to_revenue = 0
        ev_to_ebitda = data['EVToEBITDA']
        if ev_to_ebitda == "None": ev_to_ebitda = 0
        beta = data['Beta']
        if beta == "None": beta = 0
        x52_week_high = data['52WeekHigh']
        if x52_week_high == "None": x52_week_high = 0
        x52_week_low = data['52WeekLow']
        if x52_week_low == "None": x52_week_low = 0
        x50_day_moving_avg = data['50DayMovingAverage']
        if x50_day_moving_avg == "None": x50_day_moving_avg = 0
        x200_day_moving_avg = data['200DayMovingAverage']
        if x200_day_moving_avg == "None": x200_day_moving_avg = 0
        shares_outstanding = data['SharesOutstanding']
        if shares_outstanding == "None": shares_outstanding = 0
        shares_float = data['SharesFloat']
        if shares_float == "None": shares_float = 0
        shares_short = data['SharesShort']
        if shares_short == "None": shares_short = 0
        shares_short_prior_month = data['SharesShortPriorMonth']
        if shares_short_prior_month == "None": shares_short_prior_month = 0
        short_ratio = data['ShortRatio']
        if short_ratio == "None": short_ratio = 0
        short_percent_outstanding = data['ShortPercentOutstanding']
        if short_percent_outstanding == "None": short_percent_outstanding = 0
        short_percent_float = data['ShortPercentFloat']
        if short_percent_float == "None": short_percent_float = 0
        percent_insider = data['PercentInsiders']
        if percent_insider == "None": percent_insider = 0
        percent_institution = data['PercentInstitutions']
        if percent_institution == "None": percent_institution = 0
        forward_annual_div_rate = data['ForwardAnnualDividendRate']
        if forward_annual_div_rate == "None": forward_annual_div_rate = 0
        forward_annual_div_yield = data['ForwardAnnualDividendYield']
        if forward_annual_div_yield == "None": forward_annual_div_yield = 0
        payout_ratio = data['PayoutRatio']
        if payout_ratio == "None": payout_ratio = 0
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
                print(e)
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
                print(e)
    except Exception as e:
        print(e)

def update():
    cursor = db.cursor()
    try:
        cursor.execute("select uuid, symbol from security")
        results = cursor.fetchall()
        for row in results:
            uuid = row[0]
            symbol = row[1]
            update_overview(uuid, symbol)

    except Exception as e:
        print(e)
    db.close()
