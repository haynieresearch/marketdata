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
  `div_amount` float NOT NULL,
  `split_c` float NOT NULL,
  PRIMARY KEY (`uuid`),
  UNIQUE KEY `id_date` (`security_id`,`date`),
  CONSTRAINT `price_ibfk_1` FOREIGN KEY (`security_id`) REFERENCES `security` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=latin1
