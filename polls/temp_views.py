# # from django.shortcuts import render, get_object_or_404
# # from django.http import JsonResponse
# # from .models import Poll
# #
# #
# # # Create your views here.
# # def polls_list(request):
# #     MAX_OBJECTS  = 20
# #     polls = Poll.objects.all()[:20]
# #     data = {
# #         "results": list(polls.values("question", "created_by__username", "pub_date"))
# #     }
# #     return JsonResponse(data)
# #
# #
# # def polls_detail(request, pk):
# #     poll = get_object_or_404(Poll, pk=pk)
# #     data = {
# #         "results": {
# #             "quesiton": poll.question,
# #             "created_by": poll.created_by.username,
# #             "pub_date": poll.pub_date
# #         }
# #     }
# #     return JsonResponse(data)
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.views import generic
# from django.urls import reverse
#
# from .models import Poll, Choices
#
#
# # class IndexView(generic.ListView):
# #
# #     def get_queryset(self):
# #         """Return last five published questions"""
# # 	    return Poll.objects.order_by('-pub_date')
# #
# #
# # class DetailView(generic.DetailView):
# #     model = Poll
# #
# #
# # class ResultsView(generic.DetailView):
# # 	model = Poll
#
#
# def vote(request, question_id):
# 	question = get_object_or_404(Poll, pk=question_id)
# 	try:
# 		selected_choice = question.choices_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choices.DoesNotExist):
# 		#display the question voting form
# 		return ""  #  render(request, 'polls/detail.html', {'question': question, 'error_message':"You
#         #  didn't select a choice",})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		#Always submit an HttpResponseRedirect after successfully dealing with POST data
# 		#This prevents the form being posted twice if a user hits the back button
# 		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
#
# # Without Generic Views (for comparison)
#
# def index(request):
# 	latest_question_list = Poll.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list, }
# 	return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
# 	question = get_object_or_404(Poll, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
# 	question = get_object_or_404(Poll, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
# 	question = get_object_or_404(Poll, pk=question_id)
# 	try:
# 		selected_choice = question.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choices.DoesNotExist):
# 		#display the question voting form
# 		return render(request, 'polls/detail.html', {'question': question, 'error_message':"You didn't select a choice",})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		#Always submit an HttpResponseRedirect after successfully dealing with POST data
# 		#This prevents the form being posted twice if a user hits the back button
# 		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
