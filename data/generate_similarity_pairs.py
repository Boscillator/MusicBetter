import pandas as pd
from tqdm import tqdm
from gensim.models import KeyedVectors

if __name__ == '__main__':
    print("Loading Metadata...")
    metadata = pd.read_csv('../raw_data/pretrained/lakh.csv')
    print(f"\t{len(metadata)} songs loaded")

    print("Loading embeddings...")
    emb = KeyedVectors.load_word2vec_format('../raw_data/pretrained/lmd.bin')
    print("\tDone!")

    ids = [i for i in metadata.id.tolist() if i in emb]

    print("Calculating and writing output")
    with open('../raw_data/pretrained/similarity.csv', 'w') as out:
        for id in tqdm(ids):
            matches = emb.most_similar(positive=[id], topn=30)
            for match, similarity in matches:
                if match.startswith('g'):
                    continue    # exclude matches from other datasets
                out.write(f'{id},{match},{similarity}\n')
    