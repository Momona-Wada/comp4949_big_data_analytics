from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView


# Create your views here.
def homePageView(request):
    return render(request, "home.html")

def aboutPageView(request):
    return render(request, "about.html")

def momonaPageView(request):
    return render(request, "momona.html")