CREATE TABLE `currency` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `currency` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1

CREATE TABLE `type` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1

CREATE TABLE `exchange` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `exchange` varchar(50) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1

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
) ENGINE=InnoDB AUTO_INCREMENT=6266 DEFAULT CHARSET=latin1

CREATE TABLE `price` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `security_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `open` float NOT NULL,
  `high` float NOT NULL,
  `low` float NOT NULL,
  `close` float NOT NULL,
  `adj_close` float NOT NULL,
  `volume` float NOT NULL,
  `div_amt` float NOT NULL,
  `split_c` float NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `id_date` (`security_id`,`date`),
  CONSTRAINT `price_ibfk_1` FOREIGN KEY (`security_id`) REFERENCES `security` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=5380 DEFAULT CHARSET=latin1

CREATE TABLE `technical` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `security_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `sma` float NOT NULL,
  `ema` float NOT NULL,
  `macd` float NOT NULL,
  `macd_signal` float NOT NULL,
  `macd_hist` float NOT NULL,
  `stoch_slow_d` float NOT NULL,
  `stoch_slow_k` float NOT NULL,
  `rsi` float NOT NULL,
  `stochrsi_fast_k` float NOT NULL,
  `stochrsi_fast_d` float NOT NULL,
  `willr` float NOT NULL,
  `roc` float NOT NULL,
  `rocr` float NOT NULL,
  `bbands_lower` float NOT NULL,
  `bbands_upper` float NOT NULL,
  `bbands_middle` float NOT NULL,
  PRIMARY KEY (`uuid`),
  KEY `security_id` (`security_id`),
  CONSTRAINT `technical_ibfk_1` FOREIGN KEY (`security_id`) REFERENCES `security` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=3221 DEFAULT CHARSET=latin1

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
) ENGINE=InnoDB AUTO_INCREMENT=3883 DEFAULT CHARSET=latin1
