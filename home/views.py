from django.shortcuts import render
#from formtools.wizard.views import CookieWizardView
from .forms import ContactForm1, ContactForm2


# Create your views here.
def home(request):
    return render(request, 'home/index.html', status=200)
