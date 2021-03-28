import fetch_midi_links as fetch
from music.models import Song
import Levenshtein as lev

def assign(song):
        maxratio = 0
        maxindex = 0
        for i in range(len(difficulties)):
            ratio = lev.ratio(song.name.lower(), names[i].lower())
            if ratio > maxratio:
                maxindex = i
                maxratio = ratio
        if maxratio > 0.45:
            song.difficulty = difficulties[maxindex]

if __name__ == '__main__':
    print("Assigning difficulties to pieces")
    names, difficulties = fetch.get_names_and_difficulties()
    for song in Song.objects.all():
        assign(song)
    total_songs = Song.objects.all().count()
    assigned = Song.objects.exclude(difficulty=None)
    print(f"Assigned difficulty ratings to \t{assigned} songs out of \t{total_songs} total songs")