from django.contrib.auth.models import User

from anonymous_user.models import AnonymousVoter
from polls.models import Poll

def filter_votes(instance, is_anonymous=True):
    """ 
    Custom function to filter related voters ids 
    And return list of voters username on a poll 
       
    """
    raw_voter_list = []
    filter_voter_list = []
    for voter_id in instance:
        if is_anonymous:
            raw_voter_list.append(voter_id['anonymous_voter'])
        else:
            raw_voter_list.append(voter_id['voted_by'])


    for  voter_id in raw_voter_list:
            if voter_id is None:
                raw_voter_list.remove(voter_id)
            
    for voter_id in raw_voter_list:
        if is_anonymous:
            retrieve_user_ = AnonymousVoter.objects.get(pk=voter_id)
        else:
            retrieve_user_ = User.objects.get(pk=voter_id)
        filter_voter_list.append(retrieve_user_.username)

    return filter_voter_list


def get_poll_votes_count(queryset_params):
        vote_count = Poll.objects.get(pk=queryset_params)
        return vote_count
