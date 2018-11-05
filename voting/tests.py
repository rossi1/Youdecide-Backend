from django.test import TestCase
from voting.models import PostPoll
from django.http import request, HttpResponse

# Create your tests here.
# say, user is logged in


#### test on PostPoll how to run it on python shell

# post = PostPoll(user=request.user, 'Awesome post')
# post.save()
#
# # another user
# user = request.user
# # he hits the upvote button, 'post' is Post object
# res = post.upvote(user)
# if 'ok' in res:
#     return HttpResponse('OK')
# return HttpResponse('ALREADY_UPVOTED')