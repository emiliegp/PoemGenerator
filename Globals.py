import gzip, json
import random
import markovify
import os

def init():
    """
        Defines all the global variables that we need to use across the
        different files
    """
    global LIMERICK_ID
    LIMERICK_ID = [45482, 56697, 982, 13646, 13648, 13650]
    global CORPUS
    CORPUS = []
    for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
            poem_line = json.loads(line.strip())
            if int(poem_line['gid']) in LIMERICK_ID:
                CORPUS.append(poem_line['s'])
    
    corpus_as_string = '\n'.join(str(line) for line in CORPUS) 
    global MODEL
    MODEL = markovify.NewlineText(corpus_as_string)
    