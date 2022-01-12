"""
Definition of views.
"""

from django.core.mail import send_mail, BadHeaderError
from datetime import datetime
from django.forms.widgets import Textarea
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from My_site.settings import DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail (name, message, email, ['MiSStartp@gmail.com'], fail_silently=False,)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def portfolio(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/portfolio.html',
        {
            'title':'portfolio',
            'year':datetime.now().year,
        }
    )

def pf_box(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/pf_box.html',
        {
            'title':'pf_box',
            'works': [
                {
                    'title': 'site',
                    'text': 'text'
                },
                {
                    'title': 'Python parser',
                    'text': 'text'
                },
                {
                    'title': 'more',
                    'text': 'text'
                },
            ],
            'year':datetime.now().year,
        }
    )