from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('music/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def results(request):
    template = loader.get_template('music/submit.html')
    context = {}
    return HttpResponse(template.render(context, request))