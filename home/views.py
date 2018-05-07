from django.shortcuts import render
from formtools.wizard.views import CookieWizardView
from .forms import ContactForm1, ContactForm2


# Create your views here.
def home(request):
    return render(request, 'home/index.html', status=200)

#
# class ContactWizard(CookieWizardView):
#
#     def done(self, form_list, **kwargs):
#         # do_something_with_the_form_data(form_list)
#         # return HttpResponseRedirect('/page-to-redirect-to-when-done/')
#         return render('home/index.html', status=200)
#
#     def done(self, form_list, form_dict, **kwargs):
#         user = form_dict['user'].save()
#         credit_card = form_dict['credit_card'].save()
#         # ...
#
#
# class ContactWizard(CookieWizardView):
#     form_list = [ContactForm1, ContactForm2]
#
#
# TRANSFER_FORMS = [
#     ("step1", ContactForm1),
#     ("step2", ContactForm2),
# ]
# TRANSFER_TEMPLATES = {
#     "step1": "template/path/step1.html",
#     "step2": "template/path/step2.html"
# }
#
#
# class MyFormWizard(CookieWizardView):
#     # my awesome code
#     pass
#
# my_form_wizard_view = MyFormWizard.as_view(TRANSFER_FORMS)