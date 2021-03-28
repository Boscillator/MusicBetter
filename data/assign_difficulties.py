import fetch_midi_links as fetch
from music.models import Song
import Levenshtein as lev

names, difficulties = fetch.get_names_and_difficulties()
for song in Song.objects.all():
    maxratio = 0
    maxindex = 0
    for i in range(len(difficulties)):
        ratio = lev.ratio(song.name.lower(), names[i].lower())
        if ratio > maxratio:
            maxindex = i
            maxratio = ratio
    if maxratio > 0.45:
        song.difficulty = difficulties[maxindex]