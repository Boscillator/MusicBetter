from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PieceForm
from .models import Song, Comp

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PieceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/results/')
        else:
            template = loader.get_template('music/index.html')
            context = {}
            return HttpResponse(template.render(context, request))
    else:
        songlist = Song.objects.all
        template = loader.get_template('music/index.html')
        context = {
        'songlist' : songlist,
        }
        return HttpResponse(template.render(context, request))

def results(request):
    template = loader.get_template('music/results.html')
    context = {}
    return HttpResponse(template.render(context, request))