import pandas as pd

meta = pd.read_csv('../raw_data/pretrained/lakh.csv')
similarity = pd.read_csv('../raw_data/pretrained/similarity.csv', header=None)

lookup = {row['id']: row['song_name'] for _,row in meta.iterrows()}

similarity[0] = similarity[0].apply(lambda x: lookup.get(x))
similarity[1] = similarity[1].apply(lambda x: lookup.get(x))

similarity.dropna().to_csv('../raw_data/pretrained/similarity_by_name.csv')