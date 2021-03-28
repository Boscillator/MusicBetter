from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect, JsonResponse
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
            song_name = form.cleaned_data['piece_name']
            song = Song.objects.get(name=song_name)
            return HttpResponseRedirect(reverse('results', kwargs={'song': song.id}))
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

    user_song = Song.objects.get(id=song)
    matches = user_song.matches
    matches_filtered = matches.filter(
        similarity__gte=0.85).order_by('-similarity').all()
    context = {
        'song': user_song,
        'matches': matches_filtered
    }

    return HttpResponse(template.render(context, request))

def search_by_name(request):
    term = request.GET.get('term')
    songs = Song.objects.filter(name__startswith=term).all()
    song_names = [song.name for song in songs]
    return JsonResponse(song_names, safe=False)
