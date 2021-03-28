import Levenshtein as lev

def assign(names, difficulties, song):
    if song == None:
        return 0
    maxratio = 0
    maxindex = 0
    for i in range(len(difficulties)):
        if names[i] == None:
            continue
        ratio = lev.ratio(song.lower(), names[i].lower())
        if ratio > maxratio:
            maxindex = i
            maxratio = ratio
    if maxratio > 0.45:
        return difficulties[maxindex]
    else:
        return 0

'''
if __name__ == '__main__':
    print("Assigning difficulties to pieces")
    
    for song in Song.objects.all():
        assign(song)
    total_songs = Song.objects.all().count()
    assigned = Song.objects.exclude(difficulty=None)
    print(f"Assigned difficulty ratings to \t{assigned} songs out of \t{total_songs} total songs")
'''