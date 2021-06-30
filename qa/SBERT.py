from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

from . import OpenData

data = OpenData.getPreData()
model = SentenceTransformer('stsb-mpnet-base-v2')
# embed = np.load('qa/sbert_embed.npy')
embed = np.load('G:/_DATA/sbert_embed.npy')

def bert(query):
    query_embed = model.encode([query])       # query_vector

    similar = cosine_similarity(query_embed, embed)

    result = []
    for id, score in sorted(enumerate(similar[0]), key=lambda x: x[1], reverse=True)[0:5]:
        result.append([score, data['Question'][id], data['Answer'][id]])
    # print(pd.DataFrame(result, columns=["Score", "Prediction", "Answer"]))

    return result

