import torch
from rapidfuzz import process, utils
from sentence_transformers import SentenceTransformer

vocab = []

dataset = [
    ["передай привет андрею", "передаю привет андрею"],
    ["скажи привет олегу", "привет олегу"]
]

def normalize(text):
    return text.lower().split()

for data in dataset:
    for q, a in zip(normalize(data[0]), normalize(data[1])):
        if not q in vocab:
            vocab.append(q)

        if not a in vocab:
            vocab.append(a)


questions = [x[0] for x in dataset]


class TextGenerator:
    def __init__(self, text):
        
        pass