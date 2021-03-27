import music21
import sys
import glob
from music21 import midi
from pprint import pprint
from multiprocessing import Pool
import tqdm

def chordify(path_artist_names):
    path, (artist, name) = path_artist_names
    try:
        mf = midi.MidiFile()
        mf.open(path)
        mf.read()
        mf.close()

        s = midi.translate.midiFileToStream(mf)

        bChords = s.chordify()

        names = []
        for thisChord in bChords.recurse().getElementsByClass('Chord'):
            names.append(thisChord.pitchedCommonName)

        with open(f'..\\raw_data\\chords\\{artist}_{name}.txt', 'w') as outf:
            outf.write('\n'.join(names))

    except Exception as ex:
        print(ex)

def get_artist_name(path):
    p = path.split('\\')
    return p[1], p[2]

if __name__ == '__main__':
    print("Reading")
    paths = glob.glob('../raw_data/midi/**/*.mid')
    artists_and_names = [get_artist_name(path) for path in paths]
    path_artists_and_names = zip(paths, artists_and_names)
    
    print("Starting Pool")
    with Pool(20) as p:
        print("Running")
        for _ in tqdm.tqdm(p.imap_unordered(chordify, path_artists_and_names), total=len(paths)):
            pass
        