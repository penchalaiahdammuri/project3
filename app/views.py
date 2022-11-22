from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('This is your first view function')

def propose(request):
    return HttpResponse('<marquee>yes I Love You Too</marquee>')  