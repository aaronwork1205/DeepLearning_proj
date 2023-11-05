import numpy as np
import torch
import torch.nn as F
import pandas


def add_sentimental_label(data):
    sentiment_score = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1}
    sentiment = {0: 'NEGATIVE', 1: 'POSITIVE'}

    data['sentiment_score'] = data['reviews.rating'].map(sentiment_score)
    data['sentiment'] = data['sentiment_score'].map(sentiment)

    return data





