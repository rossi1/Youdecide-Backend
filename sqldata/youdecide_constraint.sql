use YOUDECIDE;

alter table `search_registry` add index IDXM7564533001 (`search_registry_id`);

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
		
alter table `survey_question` add index IDX7564533005 (`survey_question_id`),
	add constraint FKXM7564533004 foreign key (`created_by`) 
		references `users` (`users_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_choice_text` add index IDX7564533006 (`survey_choice_text_id`),
	add constraint FKX7564533007 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_choice_image` add index IDX7564533007 (`survey_choice_image_id`),
	add constraint FKX7564533008 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKXM7564533008 foreign key (`media_id`) 
		references `media` (`media_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `media_filesize` add index IDXM7564533007 (`media_filesize_id`);

alter table `media_type` add index IDXM7564533008 (`media_type_id`),
	add constraint FKXMI7564533009 foreign key (`mediafilesizeid`) 
		references `media_filesize` (`media_filesize_id`) ON DELETE CASCADE ON UPDATE CASCADE;



alter table `media` add index IDXM7564533009 (`media_id`),
	add constraint FKXM7564533009 foreign key (`mediatypeid`) 
		references `media_type` (`media_type_id`) ON DELETE CASCADE ON UPDATE CASCADE;


alter table `survey_categories` add index IDX7564533008 (`survey_categories_id`),
	add constraint FKX7564533009 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533010 foreign key (`category_id`) 
		references `category` (`category_id`) ON DELETE CASCADE ON UPDATE CASCADE;
		
alter table `survey_vote` add index IDX7564533009 (`survey_vote_id`),
	add constraint FKX7564533011 foreign key (`voter_type_id`) 
		references `voter_type` (`voter_type_id`) ON DELETE CASCADE ON UPDATE CASCADE,

	add constraint FKX7564533012 foreign key (`survey_choice_image_id`) 
		references `survey_choice_image` (`survey_choice_image_id`) ON DELETE CASCADE ON UPDATE CASCADE,

	add constraint FKXM7564533012 foreign key (`survey_choice_text_id`) 
		references `survey_choice_text` (`survey_choice_text_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533013 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `anonymous_voter` add index IDX7564533010 (`anonymous_voter_id`),

	add constraint FKXM7564533014 foreign key (`survey_choice_image_id`) 
		references `survey_choice_image` (`survey_choice_image_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKXM7564533015 foreign key (`survey_choice_text_id`) 
		references `survey_choice_text` (`survey_choice_text_id`) ON DELETE CASCADE ON UPDATE CASCADE,
	add constraint FKX7564533015 foreign key (`survey_id`) 
		references `survey_question` (`survey_question_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `action_type` add index IDX7564533011 (`action_type_id`);

alter table `state` add index IDX7564533012 (`state_id`),
	add constraint FKX7564533016 foreign key (`countryid`) 
		references `country` (`country_id`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table `city` add index IDX7564533013 (`city_id`),
	add constraint FKX7564533017 foreign key (`stateid`) 
		references `state` (`state_id`) ON DELETE CASCADE ON UPDATE CASCADE;



