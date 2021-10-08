"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
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