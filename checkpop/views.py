__author__ = 'Patrik'
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404

def home(request):
    return HttpResponse('Check. Pop.')