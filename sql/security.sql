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
