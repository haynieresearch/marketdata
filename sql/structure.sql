-- MySQL dump 10.18  Distrib 10.3.27-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: marketdata
-- ------------------------------------------------------
-- Server version	10.3.27-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `currency`
--

DROP TABLE IF EXISTS `currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `currency` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `currency` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `daily`
--

DROP TABLE IF EXISTS `daily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daily` (
  `uuid` int(20) NOT NULL AUTO_INCREMENT,
  `security_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `open` float NOT NULL,
  `high` float NOT NULL,
  `low` float NOT NULL,
  `close` float NOT NULL,
  `volume` float NOT NULL,
  `uOpen` float NOT NULL,
  `uClose` float NOT NULL,
  `uHigh` float NOT NULL,
  `uLow` float NOT NULL,
  `uVolume` float NOT NULL,
  `fOpen` float NOT NULL,
  `fClose` float NOT NULL,
  `fHigh` float NOT NULL,
  `fLow` float NOT NULL,
  `fVolume` float NOT NULL,
  `change` float NOT NULL,
  `changePercent` float NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `id_date` (`security_id`,`date`),
  CONSTRAINT `daily_ibfk_1` FOREIGN KEY (`security_id`) REFERENCES `security` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=62106040 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `exchange`
--

DROP TABLE IF EXISTS `exchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exchange` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `exchange` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `industry_price`
--

DROP TABLE IF EXISTS `industry_price`;
/*!50001 DROP VIEW IF EXISTS `industry_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `industry_price` (
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `large_cap_analysis`
--

DROP TABLE IF EXISTS `large_cap_analysis`;
/*!50001 DROP VIEW IF EXISTS `large_cap_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `large_cap_analysis` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `market_data_analysis`
--

DROP TABLE IF EXISTS `market_data_analysis`;
/*!50001 DROP VIEW IF EXISTS `market_data_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `market_data_analysis` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `market_data_fundamental`
--

DROP TABLE IF EXISTS `market_data_fundamental`;
/*!50001 DROP VIEW IF EXISTS `market_data_fundamental`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `market_data_fundamental` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `market_data_source`
--

DROP TABLE IF EXISTS `market_data_source`;
/*!50001 DROP VIEW IF EXISTS `market_data_source`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `market_data_source` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `market_price`
--

DROP TABLE IF EXISTS `market_price`;
/*!50001 DROP VIEW IF EXISTS `market_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `market_price` (
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `micro_cap_analysis`
--

DROP TABLE IF EXISTS `micro_cap_analysis`;
/*!50001 DROP VIEW IF EXISTS `micro_cap_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `micro_cap_analysis` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `mid_cap_analysis`
--

DROP TABLE IF EXISTS `mid_cap_analysis`;
/*!50001 DROP VIEW IF EXISTS `mid_cap_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `mid_cap_analysis` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `uuid` int(20) NOT NULL AUTO_INCREMENT,
  `security_id` int(11) NOT NULL,
  `datetime` varchar(20) NOT NULL,
  `headline` longtext NOT NULL,
  `source` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `summary` longtext DEFAULT NULL,
  `import_date` date DEFAULT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `security_datetime` (`security_id`,`datetime`),
  KEY `security_uuid` (`security_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7323 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `overview`
--

DROP TABLE IF EXISTS `overview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `overview` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `security_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `country` varchar(50) NOT NULL,
  `sector` varchar(255) NOT NULL,
  `industry` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `fte` int(11) NOT NULL,
  `fiscal_ye` varchar(45) NOT NULL,
  `latest_qtr` datetime NOT NULL,
  `market_cap` float NOT NULL,
  `ebitda` float NOT NULL,
  `pe_ratio` float NOT NULL,
  `peg_ratio` float NOT NULL,
  `book_value` float NOT NULL,
  `div_per_share` float NOT NULL,
  `div_yield` float NOT NULL,
  `eps` float NOT NULL,
  `revenue_per_share` float NOT NULL,
  `profit_margin` float NOT NULL,
  `ops_margin` float NOT NULL,
  `return_on_assets` float NOT NULL,
  `return_on_equity` float NOT NULL,
  `revenue` float NOT NULL,
  `gross_profit` float NOT NULL,
  `diluted_eps` float NOT NULL,
  `qtr_earnings_growth_yoy` float NOT NULL,
  `qtr_revenue_growth_yoy` float NOT NULL,
  `analyst_target_price` float NOT NULL,
  `trailing_pe` float NOT NULL,
  `forward_pe` float NOT NULL,
  `price_to_sales_ratio` float NOT NULL,
  `price_to_book_ratio` float NOT NULL,
  `ev_to_revenue` float NOT NULL,
  `ev_to_ebitda` float NOT NULL,
  `beta` float NOT NULL,
  `52_week_high` float NOT NULL,
  `52_week_low` float NOT NULL,
  `50_day_moving_avg` float NOT NULL,
  `200_day_moving_avg` float NOT NULL,
  `shares_outstanding` float NOT NULL,
  `shares_float` float NOT NULL,
  `shares_short` float NOT NULL,
  `shares_short_prior_month` float NOT NULL,
  `short_ratio` float NOT NULL,
  `short_percent_outstanding` float NOT NULL,
  `short_percent_float` float NOT NULL,
  `percent_insider` float NOT NULL,
  `percent_institution` float NOT NULL,
  `forward_annual_div_rate` float NOT NULL,
  `forward_annual_div_yield` float NOT NULL,
  `payout_ratio` float NOT NULL,
  `div_date` datetime NOT NULL,
  `ex_div_date` datetime NOT NULL,
  `last_split_factor` varchar(10) NOT NULL,
  `last_split_date` datetime NOT NULL,
  PRIMARY KEY (`uuid`),
  KEY `security_id` (`security_id`),
  CONSTRAINT `overview_ibfk_1` FOREIGN KEY (`security_id`) REFERENCES `security` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4738 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `sector_price`
--

DROP TABLE IF EXISTS `sector_price`;
/*!50001 DROP VIEW IF EXISTS `sector_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `sector_price` (
  `sector` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `security`
--

DROP TABLE IF EXISTS `security`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `security` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(45) NOT NULL,
  `type_id` int(11) NOT NULL,
  `exchange_id` int(11) NOT NULL,
  `currency_id` int(11) NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `symbol` (`symbol`),
  KEY `type_id` (`type_id`),
  KEY `exchange_id` (`exchange_id`),
  KEY `currency_id` (`currency_id`),
  CONSTRAINT `security_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `type` (`uuid`),
  CONSTRAINT `security_ibfk_2` FOREIGN KEY (`exchange_id`) REFERENCES `exchange` (`uuid`),
  CONSTRAINT `security_ibfk_3` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=12751 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `security_obs`
--

DROP TABLE IF EXISTS `security_obs`;
/*!50001 DROP VIEW IF EXISTS `security_obs`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `security_obs` (
  `obs` tinyint NOT NULL,
  `uuid` tinyint NOT NULL,
  `symbol` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `security_overview`
--

DROP TABLE IF EXISTS `security_overview`;
/*!50001 DROP VIEW IF EXISTS `security_overview`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `security_overview` (
  `uuid` tinyint NOT NULL,
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `52_week_high` tinyint NOT NULL,
  `52_week_low` tinyint NOT NULL,
  `50_day_moving_avg` tinyint NOT NULL,
  `200_day_moving_avg` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `div_date` tinyint NOT NULL,
  `ex_div_date` tinyint NOT NULL,
  `last_split_factor` tinyint NOT NULL,
  `last_split_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `security_price`
--

DROP TABLE IF EXISTS `security_price`;
/*!50001 DROP VIEW IF EXISTS `security_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `security_price` (
  `uuid` tinyint NOT NULL,
  `symbol` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `type` tinyint NOT NULL,
  `exchange` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `price_update_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `security_segment`
--

DROP TABLE IF EXISTS `security_segment`;
/*!50001 DROP VIEW IF EXISTS `security_segment`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `security_segment` (
  `obs` tinyint NOT NULL,
  `uuid` tinyint NOT NULL,
  `symbol` tinyint NOT NULL,
  `segment` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `security_technical`
--

DROP TABLE IF EXISTS `security_technical`;
/*!50001 DROP VIEW IF EXISTS `security_technical`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `security_technical` (
  `uuid` tinyint NOT NULL,
  `symbol` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `technical_update_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `small_cap_analysis`
--

DROP TABLE IF EXISTS `small_cap_analysis`;
/*!50001 DROP VIEW IF EXISTS `small_cap_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `small_cap_analysis` (
  `symbol` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `sector` tinyint NOT NULL,
  `industry` tinyint NOT NULL,
  `open` tinyint NOT NULL,
  `high` tinyint NOT NULL,
  `low` tinyint NOT NULL,
  `close` tinyint NOT NULL,
  `adj_close` tinyint NOT NULL,
  `volume` tinyint NOT NULL,
  `dividend_amount` tinyint NOT NULL,
  `split_coefficient` tinyint NOT NULL,
  `fte` tinyint NOT NULL,
  `fiscal_ye` tinyint NOT NULL,
  `latest_qtr` tinyint NOT NULL,
  `market_cap` tinyint NOT NULL,
  `ebitda` tinyint NOT NULL,
  `pe_ratio` tinyint NOT NULL,
  `peg_ratio` tinyint NOT NULL,
  `book_value` tinyint NOT NULL,
  `div_per_share` tinyint NOT NULL,
  `div_yield` tinyint NOT NULL,
  `eps` tinyint NOT NULL,
  `revenue_per_share` tinyint NOT NULL,
  `profit_margin` tinyint NOT NULL,
  `return_on_assets` tinyint NOT NULL,
  `return_on_equity` tinyint NOT NULL,
  `revenue` tinyint NOT NULL,
  `gross_profit` tinyint NOT NULL,
  `diluted_eps` tinyint NOT NULL,
  `qtr_earnings_growth_yoy` tinyint NOT NULL,
  `qtr_revenue_growth_yoy` tinyint NOT NULL,
  `analyst_target_price` tinyint NOT NULL,
  `trailing_pe` tinyint NOT NULL,
  `forward_pe` tinyint NOT NULL,
  `price_to_sales_ratio` tinyint NOT NULL,
  `price_to_book_ratio` tinyint NOT NULL,
  `ev_to_revenue` tinyint NOT NULL,
  `ev_to_ebitda` tinyint NOT NULL,
  `beta` tinyint NOT NULL,
  `week_high_52` tinyint NOT NULL,
  `week_low_52` tinyint NOT NULL,
  `moving_avg_50_day` tinyint NOT NULL,
  `moving_avg_200_day` tinyint NOT NULL,
  `shares_outstanding` tinyint NOT NULL,
  `shares_float` tinyint NOT NULL,
  `shares_short` tinyint NOT NULL,
  `shares_short_prior_month` tinyint NOT NULL,
  `short_ratio` tinyint NOT NULL,
  `short_percent_outstanding` tinyint NOT NULL,
  `short_percent_float` tinyint NOT NULL,
  `percent_insider` tinyint NOT NULL,
  `percent_institution` tinyint NOT NULL,
  `forward_annual_div_rate` tinyint NOT NULL,
  `forward_annual_div_yield` tinyint NOT NULL,
  `payout_ratio` tinyint NOT NULL,
  `sma` tinyint NOT NULL,
  `ema` tinyint NOT NULL,
  `macd` tinyint NOT NULL,
  `macd_signal` tinyint NOT NULL,
  `macd_hist` tinyint NOT NULL,
  `stoch_slow_d` tinyint NOT NULL,
  `stoch_slow_k` tinyint NOT NULL,
  `rsi` tinyint NOT NULL,
  `stochrsi_fast_d` tinyint NOT NULL,
  `stochrsi_fast_k` tinyint NOT NULL,
  `willr` tinyint NOT NULL,
  `roc` tinyint NOT NULL,
  `rocr` tinyint NOT NULL,
  `bbands_upper` tinyint NOT NULL,
  `bbands_middle` tinyint NOT NULL,
  `bbands_lower` tinyint NOT NULL,
  `refresh_date` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `industry_price`
--

/*!50001 DROP TABLE IF EXISTS `industry_price`*/;
/*!50001 DROP VIEW IF EXISTS `industry_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`marketdata`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `industry_price` AS select `security_price`.`industry` AS `industry`,sum(`security_price`.`open`) AS `open`,sum(`security_price`.`high`) AS `high`,sum(`security_price`.`low`) AS `low`,sum(`security_price`.`close`) AS `close`,`security_price`.`price_update_date` AS `date` from `security_price` where `security_price`.`industry` is not null and `security_price`.`industry` <> '' and `security_price`.`industry` <> ' ' and `security_price`.`open` > 0 and `security_price`.`high` > 0 and `security_price`.`low` > 0 and `security_price`.`close` > 0 group by `security_price`.`industry`,`security_price`.`price_update_date` order by `security_price`.`price_update_date`,`security_price`.`industry` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `large_cap_analysis`
--

/*!50001 DROP TABLE IF EXISTS `large_cap_analysis`*/;
/*!50001 DROP VIEW IF EXISTS `large_cap_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`marketdata`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `large_cap_analysis` AS select `market_data_analysis`.`symbol` AS `symbol`,`market_data_analysis`.`name` AS `name`,`market_data_analysis`.`sector` AS `sector`,`market_data_analysis`.`industry` AS `industry`,`market_data_analysis`.`open` AS `open`,`market_data_analysis`.`high` AS `high`,`market_data_analysis`.`low` AS `low`,`market_data_analysis`.`close` AS `close`,`market_data_analysis`.`adj_close` AS `adj_close`,`market_data_analysis`.`volume` AS `volume`,`market_data_analysis`.`dividend_amount` AS `dividend_amount`,`market_data_analysis`.`split_coefficient` AS `split_coefficient`,`market_data_analysis`.`fte` AS `fte`,`market_data_analysis`.`fiscal_ye` AS `fiscal_ye`,`market_data_analysis`.`latest_qtr` AS `latest_qtr`,`market_data_analysis`.`market_cap` AS `market_cap`,`market_data_analysis`.`ebitda` AS `ebitda`,`market_data_analysis`.`pe_ratio` AS `pe_ratio`,`market_data_analysis`.`peg_ratio` AS `peg_ratio`,`market_data_analysis`.`book_value` AS `book_value`,`market_data_analysis`.`div_per_share` AS `div_per_share`,`market_data_analysis`.`div_yield` AS `div_yield`,`market_data_analysis`.`eps` AS `eps`,`market_data_analysis`.`revenue_per_share` AS `revenue_per_share`,`market_data_analysis`.`profit_margin` AS `profit_margin`,`market_data_analysis`.`return_on_assets` AS `return_on_assets`,`market_data_analysis`.`return_on_equity` AS `return_on_equity`,`market_data_analysis`.`revenue` AS `revenue`,`market_data_analysis`.`gross_profit` AS `gross_profit`,`market_data_analysis`.`diluted_eps` AS `diluted_eps`,`market_data_analysis`.`qtr_earnings_growth_yoy` AS `qtr_earnings_growth_yoy`,`market_data_analysis`.`qtr_revenue_growth_yoy` AS `qtr_revenue_growth_yoy`,`market_data_analysis`.`analyst_target_price` AS `analyst_target_price`,`market_data_analysis`.`trailing_pe` AS `trailing_pe`,`market_data_analysis`.`forward_pe` AS `forward_pe`,`market_data_analysis`.`price_to_sales_ratio` AS `price_to_sales_ratio`,`market_data_analysis`.`price_to_book_ratio` AS `price_to_book_ratio`,`market_data_analysis`.`ev_to_revenue` AS `ev_to_revenue`,`market_data_analysis`.`ev_to_ebitda` AS `ev_to_ebitda`,`market_data_analysis`.`beta` AS `beta`,`market_data_analysis`.`week_high_52` AS `week_high_52`,`market_data_analysis`.`week_low_52` AS `week_low_52`,`market_data_analysis`.`moving_avg_50_day` AS `moving_avg_50_day`,`market_data_analysis`.`moving_avg_200_day` AS `moving_avg_200_day`,`market_data_analysis`.`shares_outstanding` AS `shares_outstanding`,`market_data_analysis`.`shares_float` AS `shares_float`,`market_data_analysis`.`shares_short` AS `shares_short`,`market_data_analysis`.`shares_short_prior_month` AS `shares_short_prior_month`,`market_data_analysis`.`short_ratio` AS `short_ratio`,`market_data_analysis`.`short_percent_outstanding` AS `short_percent_outstanding`,`market_data_analysis`.`short_percent_float` AS `short_percent_float`,`market_data_analysis`.`percent_insider` AS `percent_insider`,`market_data_analysis`.`percent_institution` AS `percent_institution`,`market_data_analysis`.`forward_annual_div_rate` AS `forward_annual_div_rate`,`market_data_analysis`.`forward_annual_div_yield` AS `forward_annual_div_yield`,`market_data_analysis`.`payout_ratio` AS `payout_ratio`,`market_data_analysis`.`sma` AS `sma`,`market_data_analysis`.`ema` AS `ema`,`market_data_analysis`.`macd` AS `macd`,`market_data_analysis`.`macd_signal` AS `macd_signal`,`market_data_analysis`.`macd_hist` AS `macd_hist`,`market_data_analysis`.`stoch_slow_d` AS `stoch_slow_d`,`market_data_analysis`.`stoch_slow_k` AS `stoch_slow_k`,`market_data_analysis`.`rsi` AS `rsi`,`market_data_analysis`.`stochrsi_fast_d` AS `stochrsi_fast_d`,`market_data_analysis`.`stochrsi_fast_k` AS `stochrsi_fast_k`,`market_data_analysis`.`willr` AS `willr`,`market_data_analysis`.`roc` AS `roc`,`market_data_analysis`.`rocr` AS `rocr`,`market_data_analysis`.`bbands_upper` AS `bbands_upper`,`market_data_analysis`.`bbands_middle` AS `bbands_middle`,`market_data_analysis`.`bbands_lower` AS `bbands_lower`,`market_data_analysis`.`refresh_date` AS `refresh_date` from `market_data_analysis` where `market_data_analysis`.`market_cap` > 10000000000 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `market_data_analysis`
--

/*!50001 DROP TABLE IF EXISTS `market_data_analysis`*/;
/*!50001 DROP VIEW IF EXISTS `market_data_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`marketdata`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `market_data_analysis` AS select `market_data_source`.`symbol` AS `symbol`,`market_data_source`.`name` AS `name`,`market_data_source`.`sector` AS `sector`,`market_data_source`.`industry` AS `industry`,`market_data_source`.`open` AS `open`,`market_data_source`.`high` AS `high`,`market_data_source`.`low` AS `low`,`market_data_source`.`close` AS `close`,`market_data_source`.`adj_close` AS `adj_close`,`market_data_source`.`volume` AS `volume`,`market_data_source`.`dividend_amount` AS `dividend_amount`,`market_data_source`.`split_coefficient` AS `split_coefficient`,`market_data_source`.`fte` AS `fte`,`market_data_source`.`fiscal_ye` AS `fiscal_ye`,str_to_date(`market_data_source`.`latest_qtr`,'%Y-%m-%d') AS `latest_qtr`,`market_data_source`.`market_cap` AS `market_cap`,`market_data_source`.`ebitda` AS `ebitda`,`market_data_source`.`pe_ratio` AS `pe_ratio`,`market_data_source`.`peg_ratio` AS `peg_ratio`,`market_data_source`.`book_value` AS `book_value`,`market_data_source`.`div_per_share` AS `div_per_share`,`market_data_source`.`div_yield` AS `div_yield`,`market_data_source`.`eps` AS `eps`,`market_data_source`.`revenue_per_share` AS `revenue_per_share`,`market_data_source`.`profit_margin` AS `profit_margin`,`market_data_source`.`return_on_assets` AS `return_on_assets`,`market_data_source`.`return_on_equity` AS `return_on_equity`,`market_data_source`.`revenue` AS `revenue`,`market_data_source`.`gross_profit` AS `gross_profit`,`market_data_source`.`diluted_eps` AS `diluted_eps`,`market_data_source`.`qtr_earnings_growth_yoy` AS `qtr_earnings_growth_yoy`,`market_data_source`.`qtr_revenue_growth_yoy` AS `qtr_revenue_growth_yoy`,`market_data_source`.`analyst_target_price` AS `analyst_target_price`,`market_data_source`.`trailing_pe` AS `trailing_pe`,`market_data_source`.`forward_pe` AS `forward_pe`,`market_data_source`.`price_to_sales_ratio` AS `price_to_sales_ratio`,`market_data_source`.`price_to_book_ratio` AS `price_to_book_ratio`,`market_data_source`.`ev_to_revenue` AS `ev_to_revenue`,`market_data_source`.`ev_to_ebitda` AS `ev_to_ebitda`,`market_data_source`.`beta` AS `beta`,`market_data_source`.`week_high_52` AS `week_high_52`,`market_data_source`.`week_low_52` AS `week_low_52`,`market_data_source`.`moving_avg_50_day` AS `moving_avg_50_day`,`market_data_source`.`moving_avg_200_day` AS `moving_avg_200_day`,`market_data_source`.`shares_outstanding` AS `shares_outstanding`,`market_data_source`.`shares_float` AS `shares_float`,`market_data_source`.`shares_short` AS `shares_short`,`market_data_source`.`shares_short_prior_month` AS `shares_short_prior_month`,`market_data_source`.`short_ratio` AS `short_ratio`,`market_data_source`.`short_percent_outstanding` AS `short_percent_outstanding`,`market_data_source`.`short_percent_float` AS `short_percent_float`,`market_data_source`.`percent_insider` AS `percent_insider`,`market_data_source`.`percent_institution` AS `percent_institution`,`market_data_source`.`forward_annual_div_rate` AS `forward_annual_div_rate`,`market_data_source`.`forward_annual_div_yield` AS `forward_annual_div_yield`,`market_data_source`.`payout_ratio` AS `payout_ratio`,`market_data_source`.`sma` AS `sma`,`market_data_source`.`ema` AS `ema`,`market_data_source`.`macd` AS `macd`,`market_data_source`.`macd_signal` AS `macd_signal`,`market_data_source`.`macd_hist` AS `macd_hist`,`market_data_source`.`stoch_slow_d` AS `stoch_slow_d`,`market_data_source`.`stoch_slow_k` AS `stoch_slow_k`,`market_data_source`.`rsi` AS `rsi`,`market_data_source`.`stochrsi_fast_d` AS `stochrsi_fast_d`,`market_data_source`.`stochrsi_fast_k` AS `stochrsi_fast_k`,`market_data_source`.`willr` AS `willr`,`market_data_source`.`roc` AS `roc`,`market_data_source`.`rocr` AS `rocr`,`market_data_source`.`bbands_upper` AS `bbands_upper`,`market_data_source`.`bbands_middle` AS `bbands_middle`,`market_data_source`.`bbands_lower` AS `bbands_lower`,`market_data_source`.`refresh_date` AS `refresh_date` from `market_data_source` where `market_data_source`.`close` > 0 and `market_data_source`.`market_cap` > 0 and `market_data_source`.`pe_ratio` > 0 and `market_data_source`.`ebitda` > 0 and `market_data_source`.`sma` > 0 and `market_data_source`.`macd` > 0 and `market_data_source`.`bbands_upper` > 0 and `market_data_source`.`bbands_middle` > 0 and `market_data_source`.`bbands_lower` > 0 order by `market_data_source`.`symbol` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `market_data_fundamental`
--

/*!50001 DROP TABLE IF EXISTS `market_data_fundamental`*/;
/*!50001 DROP VIEW IF EXISTS `market_data_fundamental`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`marketdata`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `market_data_fundamental` AS select `market_data_source`.`symbol` AS `symbol`,`market_data_source`.`name` AS `name`,`market_data_source`.`sector` AS `sector`,`market_data_source`.`industry` AS `industry`,`market_data_source`.`open` AS `open`,`market_data_source`.`high` AS `high`,`market_data_source`.`low` AS `low`,`market_data_source`.`close` AS `close`,`market_data_source`.`adj_close` AS `adj_close`,`market_data_source`.`volume` AS `volume`,`market_data_source`.`dividend_amount` AS `dividend_amount`,`market_data_source`.`split_coefficient` AS `split_coefficient`,`market_data_source`.`fte` AS `fte`,`market_data_source`.`fiscal_ye` AS `fiscal_ye`,`market_data_source`.`latest_qtr` AS `latest_qtr`,`market_data_source`.`market_cap` AS `market_cap`,`market_data_source`.`ebitda` AS `ebitda`,`market_data_source`.`pe_ratio` AS `pe_ratio`,`market_data_source`.`peg_ratio` AS `peg_ratio`,`market_data_source`.`book_value` AS `book_value`,`market_data_source`.`div_per_share` AS `div_per_share`,`market_data_source`.`div_yield` AS `div_yield`,`market_data_source`.`eps` AS `eps`,`market_data_source`.`revenue_per_share` AS `revenue_per_share`,`market_data_source`.`profit_margin` AS `profit_margin`,`market_data_source`.`return_on_assets` AS `return_on_assets`,`market_data_source`.`return_on_equity` AS `return_on_equity`,`market_data_source`.`revenue` AS `revenue`,`market_data_source`.`gross_profit` AS `gross_profit`,`market_data_source`.`diluted_eps` AS `diluted_eps`,`market_data_source`.`qtr_earnings_growth_yoy` AS `qtr_earnings_growth_yoy`,`market_data_source`.`qtr_revenue_growth_yoy` AS `qtr_revenue_growth_yoy`,`market_data_source`.`analyst_target_price` AS `analyst_target_price`,`market_data_source`.`trailing_pe` AS `trailing_pe`,`market_data_source`.`forward_pe` AS `forward_pe`,`market_data_source`.`price_to_sales_ratio` AS `price_to_sales_ratio`,`market_data_source`.`price_to_book_ratio` AS `price_to_book_ratio`,`market_data_source`.`ev_to_revenue` AS `ev_to_revenue`,`market_data_source`.`ev_to_ebitda` AS `ev_to_ebitda`,`market_data_source`.`beta` AS `beta`,`market_data_source`.`week_high_52` AS `week_high_52`,`market_data_source`.`week_low_52` AS `week_low_52`,`market_data_source`.`moving_avg_50_day` AS `moving_avg_50_day`,`market_data_source`.`moving_avg_200_day` AS `moving_avg_200_day`,`market_data_source`.`shares_outstanding` AS `shares_outstanding`,`market_data_source`.`shares_float` AS `shares_float`,`market_data_source`.`shares_short` AS `shares_short`,`market_data_source`.`shares_short_prior_month` AS `shares_short_prior_month`,`market_data_source`.`short_ratio` AS `short_ratio`,`market_data_source`.`short_percent_outstanding` AS `short_percent_outstanding`,`market_data_source`.`short_percent_float` AS `short_percent_float`,`market_data_source`.`percent_insider` AS `percent_insider`,`market_data_source`.`percent_institution` AS `percent_institution`,`market_data_source`.`forward_annual_div_rate` AS `forward_annual_div_rate`,`market_data_source`.`forward_annual_div_yield` AS `forward_annual_div_yield`,`market_data_source`.`payout_ratio` AS `payout_ratio`,`market_data_source`.`sma` AS `sma`,`market_data_source`.`ema` AS `ema`,`market_data_source`.`macd` AS `macd`,`market_data_source`.`macd_signal` AS `macd_signal`,`market_data_source`.`macd_hist` AS `macd_hist`,`market_data_source`.`stoch_slow_d` AS `stoch_slow_d`,`market_data_source`.`stoch_slow_k` AS `stoch_slow_k`,`market_data_source`.`rsi` AS `rsi`,`market_data_source`.`stochrsi_fast_d` AS `stochrsi_fast_d`,`market_data_source`.`stochrsi_fast_k` AS `stochrsi_fast_k`,`market_data_source`.`willr` AS `willr`,`market_data_source`.`roc` AS `roc`,`market_data_source`.`rocr` AS `rocr`,`market_data_source`.`bbands_upper` AS `bbands_upper`,`market_data_source`.`bbands_middle` AS `bbands_middle`,`market_data_source`.`bbands_lower` AS `bbands_lower`,`market_data_source`.`refresh_date` AS `refresh_date` from `market_data_source` where `market_data_source`.`close` > 0 and `market_data_source`.`market_cap` > 0 and `market_data_source`.`pe_ratio` > 0 and `market_data_source`.`ebitda` > 0 order by `market_data_source`.`symbol` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `market_data_source`
--

/*!50001 DROP TABLE IF EXISTS `market_data_source`*/;
/*!50001 DROP VIEW IF EXISTS `market_data_source`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`marketdata`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `market_data_source` AS select `p`.`symbol` AS `symbol`,`o`.`name` AS `name`,`o`.`sector` AS `sector`,`o`.`industry` AS `industry`,`p`.`open` AS `open`,`p`.`high` AS `high`,`p`.`low` AS `low`,`p`.`close` AS `close`,`p`.`adj_close` AS `adj_close`,`p`.`volume` AS `volume`,`p`.`dividend_amount` AS `dividend_amount`,`p`.`split_coefficient` AS `split_coefficient`,`o`.`fte` AS `fte`,`o`.`fiscal_ye` AS `fiscal_ye`,cast(`o`.`latest_qtr` as date) AS `latest_qtr`,`o`.`market_cap` AS `market_cap`,`o`.`ebitda` AS `ebitda`,`o`.`pe_ratio` AS `pe_ratio`,`o`.`peg_ratio` AS `peg_ratio`,`o`.`book_value` AS `book_value`,`o`.`div_per_share` AS `div_per_share`,`o`.`div_yield` AS `div_yield`,`o`.`eps` AS `eps`,`o`.`revenue_per_share` AS `revenue_per_share`,`o`.`profit_margin` AS `profit_margin`,`o`.`return_on_assets` AS `return_on_assets`,`o`.`return_on_equity` AS `return_on_equity`,`o`.`revenue` AS `revenue`,`o`.`gross_profit` AS `gross_profit`,`o`.`diluted_eps` AS `diluted_eps`,`o`.`qtr_earnings_growth_yoy` AS `qtr_earnings_growth_yoy`,`o`.`qtr_revenue_growth_yoy` AS `qtr_revenue_growth_yoy`,`o`.`analyst_target_price` AS `analyst_target_price`,`o`.`trailing_pe` AS `trailing_pe`,`o`.`forward_pe` AS `forward_pe`,`o`.`price_to_sales_ratio` AS `price_to_sales_ratio`,`o`.`price_to_book_ratio` AS `price_to_book_ratio`,`o`.`ev_to_revenue` AS `ev_to_revenue`,`o`.`ev_to_ebitda` AS `ev_to_ebitda`,`o`.`beta` AS `beta`,`o`.`52_week_high` AS `week_high_52`,`o`.`52_week_low` AS `week_low_52`,`o`.`50_day_moving_avg` AS `moving_avg_50_day`,`o`.`200_day_moving_avg` AS `moving_avg_200_day`,`o`.`shares_outstanding` AS `shares_outstanding`,`o`.`shares_float` AS `shares_float`,`o`.`shares_short` AS `shares_short`,`o`.`shares_short_prior_month` AS `shares_short_prior_month`,`o`.`short_ratio` AS `short_ratio`,`o`.`short_percent_outstanding` AS `short_percent_outstanding`,`o`.`short_percent_float` AS `short_percent_float`,`o`.`percent_insider` AS `percent_insider`,`o`.`percent_institution` AS `percent_institution`,`o`.`forward_annual_div_rate` AS `forward_annual_div_rate`,`o`.`forward_annual_div_yield` AS `forward_annual_div_yield`,`o`.`payout_ratio` AS `payout_ratio`,`t`.`sma` AS `sma`,`t`.`ema` AS `ema`,`t`.`macd` AS `macd`,`t`.`macd_signal` AS `macd_signal`,`t`.`macd_hist` AS `macd_hist`,`t`.`stoch_slow_d` AS `stoch_slow_d`,`t`.`stoch_slow_k` AS `stoch_slow_k`,`t`.`rsi` AS `rsi`,`t`.`stochrsi_fast_d` AS `stochrsi_fast_d`,`t`.`stochrsi_fast_k` AS `stochrsi_fast_k`,`t`.`willr` AS `willr`,`t`.`roc` AS `roc`,`t`.`rocr` AS `rocr`,`t`.`bbands_upper` AS `bbands_upper`,`t`.`bbands_middle` AS `bbands_middle`,`t`.`bbands_lower` AS `bbands_lower`,cast(`p`.`price_update_date` as date) AS `refresh_date` from ((`security_price` `p` left join `security_overview` `o` on(`p`.`uuid` = `o`.`uuid`)) left join `security_technical` `t` on(`p`.`uuid` = `t`.`uuid` and `p`.`price_update_date` = `t`.`technical_update_date`)) order by `p`.`price_update_date`,`p`.`symbol` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `market_price`
--

/*!50001 DROP TABLE IF EXISTS `market_price`*/;
/*!50001 DROP VIEW IF EXISTS `market_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `market_price` AS select 1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `micro_cap_analysis`
--

/*!50001 DROP TABLE IF EXISTS `micro_cap_analysis`*/;
/*!50001 DROP VIEW IF EXISTS `micro_cap_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `micro_cap_analysis` AS select 1 AS `symbol`,1 AS `name`,1 AS `sector`,1 AS `industry`,1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `adj_close`,1 AS `volume`,1 AS `dividend_amount`,1 AS `split_coefficient`,1 AS `fte`,1 AS `fiscal_ye`,1 AS `latest_qtr`,1 AS `market_cap`,1 AS `ebitda`,1 AS `pe_ratio`,1 AS `peg_ratio`,1 AS `book_value`,1 AS `div_per_share`,1 AS `div_yield`,1 AS `eps`,1 AS `revenue_per_share`,1 AS `profit_margin`,1 AS `return_on_assets`,1 AS `return_on_equity`,1 AS `revenue`,1 AS `gross_profit`,1 AS `diluted_eps`,1 AS `qtr_earnings_growth_yoy`,1 AS `qtr_revenue_growth_yoy`,1 AS `analyst_target_price`,1 AS `trailing_pe`,1 AS `forward_pe`,1 AS `price_to_sales_ratio`,1 AS `price_to_book_ratio`,1 AS `ev_to_revenue`,1 AS `ev_to_ebitda`,1 AS `beta`,1 AS `week_high_52`,1 AS `week_low_52`,1 AS `moving_avg_50_day`,1 AS `moving_avg_200_day`,1 AS `shares_outstanding`,1 AS `shares_float`,1 AS `shares_short`,1 AS `shares_short_prior_month`,1 AS `short_ratio`,1 AS `short_percent_outstanding`,1 AS `short_percent_float`,1 AS `percent_insider`,1 AS `percent_institution`,1 AS `forward_annual_div_rate`,1 AS `forward_annual_div_yield`,1 AS `payout_ratio`,1 AS `sma`,1 AS `ema`,1 AS `macd`,1 AS `macd_signal`,1 AS `macd_hist`,1 AS `stoch_slow_d`,1 AS `stoch_slow_k`,1 AS `rsi`,1 AS `stochrsi_fast_d`,1 AS `stochrsi_fast_k`,1 AS `willr`,1 AS `roc`,1 AS `rocr`,1 AS `bbands_upper`,1 AS `bbands_middle`,1 AS `bbands_lower`,1 AS `refresh_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `mid_cap_analysis`
--

/*!50001 DROP TABLE IF EXISTS `mid_cap_analysis`*/;
/*!50001 DROP VIEW IF EXISTS `mid_cap_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `mid_cap_analysis` AS select 1 AS `symbol`,1 AS `name`,1 AS `sector`,1 AS `industry`,1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `adj_close`,1 AS `volume`,1 AS `dividend_amount`,1 AS `split_coefficient`,1 AS `fte`,1 AS `fiscal_ye`,1 AS `latest_qtr`,1 AS `market_cap`,1 AS `ebitda`,1 AS `pe_ratio`,1 AS `peg_ratio`,1 AS `book_value`,1 AS `div_per_share`,1 AS `div_yield`,1 AS `eps`,1 AS `revenue_per_share`,1 AS `profit_margin`,1 AS `return_on_assets`,1 AS `return_on_equity`,1 AS `revenue`,1 AS `gross_profit`,1 AS `diluted_eps`,1 AS `qtr_earnings_growth_yoy`,1 AS `qtr_revenue_growth_yoy`,1 AS `analyst_target_price`,1 AS `trailing_pe`,1 AS `forward_pe`,1 AS `price_to_sales_ratio`,1 AS `price_to_book_ratio`,1 AS `ev_to_revenue`,1 AS `ev_to_ebitda`,1 AS `beta`,1 AS `week_high_52`,1 AS `week_low_52`,1 AS `moving_avg_50_day`,1 AS `moving_avg_200_day`,1 AS `shares_outstanding`,1 AS `shares_float`,1 AS `shares_short`,1 AS `shares_short_prior_month`,1 AS `short_ratio`,1 AS `short_percent_outstanding`,1 AS `short_percent_float`,1 AS `percent_insider`,1 AS `percent_institution`,1 AS `forward_annual_div_rate`,1 AS `forward_annual_div_yield`,1 AS `payout_ratio`,1 AS `sma`,1 AS `ema`,1 AS `macd`,1 AS `macd_signal`,1 AS `macd_hist`,1 AS `stoch_slow_d`,1 AS `stoch_slow_k`,1 AS `rsi`,1 AS `stochrsi_fast_d`,1 AS `stochrsi_fast_k`,1 AS `willr`,1 AS `roc`,1 AS `rocr`,1 AS `bbands_upper`,1 AS `bbands_middle`,1 AS `bbands_lower`,1 AS `refresh_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `sector_price`
--

/*!50001 DROP TABLE IF EXISTS `sector_price`*/;
/*!50001 DROP VIEW IF EXISTS `sector_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `sector_price` AS select 1 AS `sector`,1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `security_obs`
--

/*!50001 DROP TABLE IF EXISTS `security_obs`*/;
/*!50001 DROP VIEW IF EXISTS `security_obs`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `security_obs` AS select 1 AS `obs`,1 AS `uuid`,1 AS `symbol` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `security_overview`
--

/*!50001 DROP TABLE IF EXISTS `security_overview`*/;
/*!50001 DROP VIEW IF EXISTS `security_overview`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `security_overview` AS select 1 AS `uuid`,1 AS `symbol`,1 AS `name`,1 AS `sector`,1 AS `industry`,1 AS `fte`,1 AS `fiscal_ye`,1 AS `latest_qtr`,1 AS `market_cap`,1 AS `ebitda`,1 AS `pe_ratio`,1 AS `peg_ratio`,1 AS `book_value`,1 AS `div_per_share`,1 AS `div_yield`,1 AS `eps`,1 AS `revenue_per_share`,1 AS `profit_margin`,1 AS `return_on_assets`,1 AS `return_on_equity`,1 AS `revenue`,1 AS `gross_profit`,1 AS `diluted_eps`,1 AS `qtr_earnings_growth_yoy`,1 AS `qtr_revenue_growth_yoy`,1 AS `analyst_target_price`,1 AS `trailing_pe`,1 AS `forward_pe`,1 AS `price_to_sales_ratio`,1 AS `price_to_book_ratio`,1 AS `ev_to_revenue`,1 AS `ev_to_ebitda`,1 AS `beta`,1 AS `52_week_high`,1 AS `52_week_low`,1 AS `50_day_moving_avg`,1 AS `200_day_moving_avg`,1 AS `shares_outstanding`,1 AS `shares_float`,1 AS `shares_short`,1 AS `shares_short_prior_month`,1 AS `short_ratio`,1 AS `short_percent_outstanding`,1 AS `short_percent_float`,1 AS `percent_insider`,1 AS `percent_institution`,1 AS `forward_annual_div_rate`,1 AS `forward_annual_div_yield`,1 AS `payout_ratio`,1 AS `div_date`,1 AS `ex_div_date`,1 AS `last_split_factor`,1 AS `last_split_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `security_price`
--

/*!50001 DROP TABLE IF EXISTS `security_price`*/;
/*!50001 DROP VIEW IF EXISTS `security_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `security_price` AS select 1 AS `uuid`,1 AS `symbol`,1 AS `sector`,1 AS `industry`,1 AS `type`,1 AS `exchange`,1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `adj_close`,1 AS `volume`,1 AS `dividend_amount`,1 AS `split_coefficient`,1 AS `price_update_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `security_segment`
--

/*!50001 DROP TABLE IF EXISTS `security_segment`*/;
/*!50001 DROP VIEW IF EXISTS `security_segment`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `security_segment` AS select 1 AS `obs`,1 AS `uuid`,1 AS `symbol`,1 AS `segment` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `security_technical`
--

/*!50001 DROP TABLE IF EXISTS `security_technical`*/;
/*!50001 DROP VIEW IF EXISTS `security_technical`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `security_technical` AS select 1 AS `uuid`,1 AS `symbol`,1 AS `sma`,1 AS `ema`,1 AS `macd`,1 AS `macd_signal`,1 AS `macd_hist`,1 AS `stoch_slow_d`,1 AS `stoch_slow_k`,1 AS `rsi`,1 AS `stochrsi_fast_d`,1 AS `stochrsi_fast_k`,1 AS `willr`,1 AS `roc`,1 AS `rocr`,1 AS `bbands_upper`,1 AS `bbands_middle`,1 AS `bbands_lower`,1 AS `technical_update_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `small_cap_analysis`
--

/*!50001 DROP TABLE IF EXISTS `small_cap_analysis`*/;
/*!50001 DROP VIEW IF EXISTS `small_cap_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `small_cap_analysis` AS select 1 AS `symbol`,1 AS `name`,1 AS `sector`,1 AS `industry`,1 AS `open`,1 AS `high`,1 AS `low`,1 AS `close`,1 AS `adj_close`,1 AS `volume`,1 AS `dividend_amount`,1 AS `split_coefficient`,1 AS `fte`,1 AS `fiscal_ye`,1 AS `latest_qtr`,1 AS `market_cap`,1 AS `ebitda`,1 AS `pe_ratio`,1 AS `peg_ratio`,1 AS `book_value`,1 AS `div_per_share`,1 AS `div_yield`,1 AS `eps`,1 AS `revenue_per_share`,1 AS `profit_margin`,1 AS `return_on_assets`,1 AS `return_on_equity`,1 AS `revenue`,1 AS `gross_profit`,1 AS `diluted_eps`,1 AS `qtr_earnings_growth_yoy`,1 AS `qtr_revenue_growth_yoy`,1 AS `analyst_target_price`,1 AS `trailing_pe`,1 AS `forward_pe`,1 AS `price_to_sales_ratio`,1 AS `price_to_book_ratio`,1 AS `ev_to_revenue`,1 AS `ev_to_ebitda`,1 AS `beta`,1 AS `week_high_52`,1 AS `week_low_52`,1 AS `moving_avg_50_day`,1 AS `moving_avg_200_day`,1 AS `shares_outstanding`,1 AS `shares_float`,1 AS `shares_short`,1 AS `shares_short_prior_month`,1 AS `short_ratio`,1 AS `short_percent_outstanding`,1 AS `short_percent_float`,1 AS `percent_insider`,1 AS `percent_institution`,1 AS `forward_annual_div_rate`,1 AS `forward_annual_div_yield`,1 AS `payout_ratio`,1 AS `sma`,1 AS `ema`,1 AS `macd`,1 AS `macd_signal`,1 AS `macd_hist`,1 AS `stoch_slow_d`,1 AS `stoch_slow_k`,1 AS `rsi`,1 AS `stochrsi_fast_d`,1 AS `stochrsi_fast_k`,1 AS `willr`,1 AS `roc`,1 AS `rocr`,1 AS `bbands_upper`,1 AS `bbands_middle`,1 AS `bbands_lower`,1 AS `refresh_date` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-03 13:13:04
