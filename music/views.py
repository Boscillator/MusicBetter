from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .forms import PieceForm
from .models import Song, Comp


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PieceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            song = form.cleaned_data['piece_name']
            return HttpResponseRedirect(reverse('results', kwargs={'song': song}))
        else:
            template = loader.get_template('music/index.html')
            context = {
                'error': True
            }
            return HttpResponse(template.render(context, request))
    else:
        songlist = Song.objects.all
        template = loader.get_template('music/index.html')
        form = PieceForm()
        context = {
            'songlist': songlist,
            'form': form
        }
        return HttpResponse(template.render(context, request))


def results(request, song):
    template = loader.get_template('music/results.html')
    # Get object matching song query

    if request.method != 'GET':
        raise Exception('Should be a GET request')

    queryset = Song.objects.all()  # Need to preload csvs as Song and Comp objects
    name = song
    if name is None:
        raise Exception('name cannot be None')
    user_song = queryset.get(name=name)
    matches = user_song.matches
    matches_filtered = matches.filter(
        similarity__lte=0.85).order_by('-similarity')
    context = {
        'matches': matches_filtered
        # Gives a list of Comp objects - can then use each one's song2
    }

    return HttpResponse(template.render(context, request))
