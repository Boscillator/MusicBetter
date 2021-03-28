import pandas as pd
import sqlite3

con = sqlite3.connect('../db.sqlite3')

meta = pd.read_csv('../raw_data/pretrained/lakh.csv')
similarity = pd.read_csv('../raw_data/pretrained/similarity.csv', header=None)

print("SONGS")
print("\tExtract")
meta = meta[['id','song_name', 'album_name', 'artist_name', 'tag_echo', 'tag_mbz', 'year']]
print("\tRename")
meta.rename(columns={
    'song_name': 'name',
    'album_name': 'album',
    'artist_name': 'artist',
    'tag_echo': 'style',
    'tag_mbz': 'genera',
}, inplace=True)
print("\tLocal Insert")
meta.to_sql('music_song', con, if_exists='replace', index=False)
print("\tCSV Export")
meta.to_csv('../raw_data/db/music_song.csv', header=False, index=False)

print("COMP")
print("\tRename")
similarity.rename(columns={
    0: 'song1_id',
    1: 'song2_id',
    2: 'similarity'
}, inplace=True)
print(similarity)

print("\tLocal Insert")
similarity.to_sql('music_comp', con, if_exists='replace', index=False)

print("\tCSV Export")


