# create key algorithms for the project

import base64
import random
from functools import lru_cache


def rank_corr(pairs):
    pass


# set the width of the key
default_size = 2


def make_token(size=default_size):
    '''Computes an access token to an api randomly none deterministic.
    this test should always fail becuase is random value generation
    : param size: the width of the bytes
    : returns: a random token
    >>> make_token()
    'HolVbXih4xm3dxBQORJMthVSW6jAv13zQsAs6p5FWFavB8Kr'
    '''
    random_seed = random.SystemRandom()
    token_bytes = bytes(random_seed.randrange(0, 256) for index in range(18 * size))
    token_base64 = base64.urlsafe_b64encode(token_bytes)
    token_string = token_base64.decode('ascii')
    return token_string


# my_token = make_token()
# # print(base64.urlsafe_b64decode(my_token))
# print(my_token)
#
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()