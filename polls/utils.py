
def filter_votes(instance, is_anonymous=True):
    """ 
    Custom function to filter related voters ids 
    And return list of voters username on a poll 
       
    """
    voter_list = []

    for voter_id in instance:
            for value in voter_id.values():
                if value is None:
                    continue
                else:
                    voter_list.append(value)
    
    return voter_list
