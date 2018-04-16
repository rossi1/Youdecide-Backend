from django.db import models

# Create your models here.
'''
///
the user model will have the following objects:
USER:- EMAIL, PASSWORD, USERNAME
VOTER- VOTER-ID, VOTER IP-ADDRESS
POLL:-  CREATOR(USER), QUESTION, LOCATION, WHEN_CREATED, APPROVAL-BOOLEAN
QUESTION:- QUESTION, OPTIONS, QUESTION_ID(OR SLUG for URL for sharing)
CHOICES:- {OPTION_A: [A_COUNTS, A_PERCENT], OPTION_B: [B_COUNTS, B_PERCENT], ..., OPTION_N:
            [N_COUNTS, N_PERCENT]}
RULES:-APPROVAL, FILTER- SIMILAR POLLS!!!
RESULT or SUMMARY:- CHOICES,  WHEN_CREATED, START_DATE, END_DATE, TOTAL_VOTES,
POLLS: LIST OF POLL -


/// stackover flow answer on preventing duplicate voting


Depends on how far you want to take it:

    Submit the votes through ajax using POST method so there is no url to access directly from a browser
    Add cookies for those who voted
    Add captcha
    Store IPs (here are some suggestions on how to store them efficiently, can also utilize something
    like Redis if performance is critical, but unless you are building a national voting system you probably would be
    just fine with a regular table)
    Require registration to vote (registration with email confirmation, registration with facebook account,
    registration with sms confirmation, and so on)


    "save the vote and thank the voter"

Also whenever you detected a user has already voted, it could be a smart move to just silently ignore their further
votes and pretend that they were accepted, this way they won't try nearly as hard to cheat.

///





polls
'''