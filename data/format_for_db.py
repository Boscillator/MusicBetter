import pandas as pd
import sqlite3
import fetch_midi_links
import assign_difficulties

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
meta['difficulty'] = 0
names, difficulties = fetch_midi_links.get_names_and_difficulties()
for i,row in meta.iterrows():
    meta.at[i, 'difficulty'] = assign_difficulties.assign(names, difficulties, row['name'])
print("\tLocal Insert")
meta.to_sql('music_song', con, if_exists='replace', index=False)
print("\tCSV Export")
meta.to_csv('../raw_data/db/music_song.csv', header=False, index=False)

print("COMP")
print("\tReset Index")
similarity.reset_index(inplace=True)
print("\tRename")
similarity.rename(columns={
    'index': 'id',
    0: 'song1_id',
    1: 'song2_id',
    2: 'similarity'
}, inplace=True)
print(similarity)

print("\tLocal Insert")
similarity.to_sql('music_comp', con, if_exists='replace', index=False)

print("\tCSV Export")


