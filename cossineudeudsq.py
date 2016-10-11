# This program calculates the dictionaries of unweighted cosine similarity, sine dissimilarity, Euclidean distance and squared Euclidean distance for each window. 
from __future__ import division
import math, csv, cPickle as pickle
from mylibrary import concatenate, normalise, zerovect, dot, invert, euclideansq
from lists import words, contexts, windows

# load the distribution dictionary
with open ('dstr.pickle', 'rb') as dstrsave:
    dstr = pickle.load(dstrsave)

# remove words with zeros and normalise the rest
vectofzero = [0]*len(contexts)
wordswithzero = []
dstrofwordswithzero = {}
words_nonzero = []
dstr_nonzero_norm = {}
for i, word in enumerate(words):
    vs = dstr[word]
    if vectofzero in vs:
        wordswithzero.append([i,word])
        dstrofwordswithzero[word] = vs
    else:
        dstr_nonzero_norm[word] = []
        for j in range(len(windows)):
            dstr_nonzero_norm[word].append(normalise(vs[j]))
        words_nonzero.append(word)

# dump words_nonzero
with open('words_nonzero.pickle','wb') as words_nonzerosave:
    pickle.dump(words_nonzero, words_nonzerosave)

# calculate the similarities and distances for each window
cos = {}
sin = {}
eud = {}
eudsq = {}
for word1 in words_nonzero:
    cos[word1] = []
    sin[word1] = []
    eud[word1] = []
    eudsq[word1] = []
    for j in range(len(windows)):
        cos[word1].append([])
        sin[word1].append([])
        eud[word1].append([])
        eudsq[word1].append([])
        for word2 in words_nonzero:
            cosine = dot(dstr_nonzero_norm[word1][j],dstr_nonzero_norm[word2][j])
            if cosine > 1.0:
                cos[word1][j].append(1)
                sin[word1][j].append(0)
            elif cosine < 0.00001:
                cos[word1][j].append(0)
                sin[word1][j].append(1)
            else:
                cos[word1][j].append(cosine)
                sin[word1][j].append(math.sqrt(1-cosine**2))
            eud2 = euclideansq(dstr_nonzero_norm[word1][j],dstr_nonzero_norm[word2][j])
            eud1 = math.sqrt(eud2)
            if eud2 > 2.0:
                eud[word1][j].append(math.sqrt(2))
                eudsq[word1][j].append(2)
            elif eud2 < 0.00001:
                eud[word1][j].append(0)
                eudsq[word1][j].append(0)
            else:
                eud[word1][j].append(eud1)
                eudsq[word1][j].append(eud2)

# dump cos, sin and eudsq
with open('cos.pickle','wb') as cossave:
    pickle.dump(cos, cossave)
with open('sin.pickle','wb') as sinsave:
    pickle.dump(sin,sinsave)
with open('eud.pickle','wb') as eudsave:
    pickle.dump(eud,eudsave)
with open('eudsq.pickle','wb') as eudsqsave:
    pickle.dump(eudsq, eudsqsave)