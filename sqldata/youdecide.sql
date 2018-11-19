DROP DATABASE IF EXISTS YOUDECIDE;
CREATE DATABASE YOUDECIDE;
USE YOUDECIDE;


CREATE TABLE `search_registry` 
(
  `search_registry_id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(255) NOT NULL,
  `tags` varchar(255),
  `tablename` varchar(255) DEFAULT NULL, #represent the name of the table where search action linked to
  `rowid` int(11) DEFAULT NULL, #represents the row id of the search column
  `logTime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`search_registry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS `country` (
  `country_id` int(11) NOT NULL AUTO_INCREMENT,
  `shortcode_2` char(6) NOT NULL,
  `countryname` varchar(80) NOT NULL,
  `nickname` varchar(80) DEFAULT NULL,
  `shortcode_3` varchar(6) DEFAULT NULL,
  `numcode` smallint(6) DEFAULT NULL,
  `phone_code` int(5) DEFAULT NULL,
  PRIMARY KEY (`country_id`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `state` (
  `state_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `countryid` int(11) NOT NULL, #makes referrence to country table on id column
  PRIMARY KEY (`state_id`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS `city` (
  `city_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `stateid` int(11) NOT NULL, #makes referrence to state table on id column 
  PRIMARY KEY (`city_id`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS `timezone` (
  `timezone_id` int(11) NOT NULL,
  `CountryCode` char(6) NOT NULL,
  `Coordinates` char(15) NOT NULL,
  `timezone` char(32) NOT NULL,
  `comments` varchar(85) NOT NULL,
  `UTCoffset` char(8) NOT NULL,
  `UTCDSToffset` char(8) NOT NULL,
  `notes` varchar(79) DEFAULT NULL,
  PRIMARY KEY (`timezone_id`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS `currency` (
  `currency_id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(100) NOT NULL, 
  `currencyname` varchar(50) NOT NULL, 
  `currencycode` varchar(50),
  `currencysymbol` varchar(20),
  PRIMARY KEY (`currency_id`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;



CREATE TABLE `users` (
  `users_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(255) NOT NULL,
  `usertypeid` int(11) NOT NULL,# makes referrence to user_type table on id column
  `userstatus` tinyint(1) DEFAULT '0' COMMENT ' ''0=Inactive, 1=active, 2=blocked, 3=suspended''',
  `createddate` datetime DEFAULT CURRENT_TIMESTAMP,
  `lastupdated` datetime DEFAULT NULL,
  UNIQUE KEY(`username`),
  PRIMARY KEY (`users_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;



CREATE TABLE `user_type` (
  `user_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text,
  `createddate` datetime DEFAULT CURRENT_TIMESTAMP,
  `lastupdated` datetime DEFAULT NULL,
  primary key (`user_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;

CREATE TABLE `user_account_recovery`(
  `user_account_recovery_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL, # makes referrence to users table on id column
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `createddate` datetime DEFAULT CURRENT_TIMESTAMP,
  primary key (`user_account_recovery_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;

CREATE TABLE `action_type` (
  `action_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `actionname` varchar(20) NOT NULL,
  `description` text,
  `createddate` datetime DEFAULT CURRENT_TIMESTAMP,
  `changedate` datetime DEFAULT NULL,
  PRIMARY KEY (`action_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;

CREATE TABLE `auditvault` (
  `auditvault_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL, # makes referrence to users table on id column
  `actiontypeid` int(11) NOT NULL, # makes referrence to action_type table on id column
  `tablename` varchar(25) DEFAULT NULL, #represent the name of the table(s) where action was effected
  `useragent` text DEFAULT NULL, 
  `rowDataOld` blob,
  `rowDataNew` blob,
  `logTime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`auditvault_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;



CREATE TABLE `survey_question`(
	`survey_question_id` int(11) NOT NULL AUTO_INCREMENT, 
	`question` text NOT NULL,
	`opening_time` datetime NOT NULL, 
	`closing_time` datetime NOT NULL, 
	`created_by` int(11) NOT NULL, # makes reference to users table on id column
	`created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY(`survey_question_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


CREATE TABLE `survey_choice` (
	`survey_choice_id` int(11) NOT NULL AUTO_INCREMENT, 
	`survey_id` int(11) NOT NULL, # makes reference to survey_question table on id
	`option` text NOT NULL,
   PRIMARY KEY(`survey_choice_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


CREATE TABLE `survey_choice_image` (
	`survey_choice_image_id` int(11) NOT NULL AUTO_INCREMENT, 
	`survey_choice_id` int(11) NOT NULL, # makes reference to survey_choice table on id
	`mediafilename` varchar(50) NOT NULL,
  	`mediasource` varchar(80) DEFAULT NULL,
  	`media` longblob,
   PRIMARY KEY(`survey_choice_image_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


CREATE TABLE `category` (
	`category_id` int(11) NOT NULL AUTO_INCREMENT, 
	`title` varchar(255) NOT NULL, 
	`description` text,
  	`created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
   PRIMARY KEY(`category_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


INSERT INTO `category` (`title`,`description`) VALUES
('Politics', 'Political Survey'),
('Health', 'Health Survey'),
('Fashion', 'Fashion Survey'),
('Education', 'Education Survey'),
('Agricalture', 'Agricalture Survey'),
('Technology', 'Technology Survey'),
('Economy', 'Economy Survey'),
('Banking', 'Banking Survey'),
('Sports', 'Sports Survey');
--
CREATE TABLE `survey_categories` (
	`survey_categories_id` int(11) NOT NULL AUTO_INCREMENT, 
	`survey_id` int(11) NOT NULL, # makes reference to survey_question table on id
	`category_id` int(11), # makes reference to category table on id
   UNIQUE KEY(`survey_id`,`category_id`),
   PRIMARY KEY(`survey_categories_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;




CREATE TABLE `survey_vote` (
	`survey_vote_id` int(11) NOT NULL AUTO_INCREMENT, 
	`voter_type_id` int(11) NOT NULL, # makes reference to voter_type table on id column
	`voter_user_id` int(11) NOT NULL,
	`survey_choice_id` int(11) NOT NULL, # makes reference to survey_choice table on id coulumn
	`survey_id` int(11) NOT NULL, # makes reference to survey_question table on id
	`created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
   UNIQUE KEY(`voter_type_id`,`voter_user_id`,`survey_id`),
   PRIMARY KEY(`survey_vote_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;



CREATE TABLE `voter_type` (
	`voter_type_id` int(11) NOT NULL AUTO_INCREMENT, 
	#`survey_id` int(11) NOT NULL, # makes reference to survey_question table on id
	`title` enum('anonymous', 'user') NOT NULL DEFAULT 'anonymous',
	`created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
   PRIMARY KEY(`voter_type_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


CREATE TABLE `anonymous_voter` (
	`anonymous_voter_id` int(11) NOT NULL AUTO_INCREMENT, 
	`username` varchar(60) NOT NULL,
	`phone_number` varchar(16) NOT NULL, 
	`email_address` varchar(255),
	`survey_choice_id` int(11) NOT NULL, # makes reference to survey_choice table on id column
	`survey_id` int(11) NOT NULL, # makes reference to survey_question table on id column
	`userAgent` text,
	`deviceName` varchar(60),
	`manufacturer` varchar(60),
	`ip_address` varchar(40),
	`browserName` varchar(30),
	`browserVersion` varchar(10),
	`operatingSystem` varchar(20),
	`language` varchar(5),
	`created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
   PRIMARY KEY(`anonymous_voter_id`),
   UNIQUE KEY(`phone_number`,`survey_id`),
   UNIQUE KEY(`email_address`),
   UNIQUE KEY(`email_address`,`survey_id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8Mb4 AUTO_INCREMENT=1;


alter table `search_registry` add index IDX7564533001 (`search_registry_id`);

alter table `users` add index IDX7564533002 (`users_id`),
	add constraint FKX7564533002 foreign key (`usertypeid`) 
		references `user_type` (`user_type_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `user_account_recovery` add index IDX7564533003 (`user_account_recovery_id`),
	add constraint FKX7564533003 foreign key (`userid`) 
		references `users` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `auditvault` add index IDX7564533004 (`auditvault_id`),
	add constraint FKX7564533004 foreign key (`userid`) 
		references `users` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533005 foreign key (`actiontypeid`) 
		references `action_type` (`action_type_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_question` add index IDX7564533005 (`survey_question_id`);
		
alter table `survey_choice` add index IDX7564533006 (`survey_choice_id`),
	add constraint FKX7564533007 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_choice_image` add index IDX7564533007 (`survey_choice_image_id`),
	add constraint FKX7564533008 foreign key (`survey_choice_id`) 
		references `survey_choice` (`survey_choice_id`) ON DELETE CASCADE ON UPDATE CASCADE;


alter table `survey_categories` add index IDX7564533008 (`survey_categories_id`),
	add constraint FKX7564533009 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533010 foreign key (`category_id`) 
		references `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_vote` add index IDX7564533009 (`survey_vote_id`),
	add constraint FKX7564533011 foreign key (`voter_type_id`) 
		references `voter_type` (`voter_type_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533012 foreign key (`survey_choice_id`) 
		references `survey_choice` (`survey_choice_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533013 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `anonymous_voter` add index IDX7564533010 (`anonymous_voter_id`),		
	add constraint FKX7564533014 foreign key (`survey_choice_id`) 
		references `survey_choice` (`survey_choice_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533015 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `action_type` add index IDX7564533011 (`action_type_id`);

alter table `state` add index IDX7564533012 (`state_id`),
	add constraint FKX7564533016 foreign key (`countryid`) 
		references `country` (`country_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `city` add index IDX7564533013 (`city_id`),
	add constraint FKX7564533017 foreign key (`stateid`) 
		references `state` (`state_id`) ON DELETE CASCADE ON UPDATE CASCADE;

