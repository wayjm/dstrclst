# Adding a eud_b_weighted, which, unlike eud_weighted, is obtained by calculating the square root of weighted Euclidean distance squared. 
# This program calculates the weighted cosine, sine, Euclidean distance and Euclidean distance squared. 
import math, csv, cPickle as pickle
from mylibrary import invert, parseinterval, weightedavg
from lists import windows

# load words_nonzero, cos, sin
with open('words_nonzero.pickle','rb') as words_nonzerosave:
    words_nonzero = pickle.load(words_nonzerosave)
with open('cos.pickle','rb') as cossave:
    cos = pickle.load(cossave)
with open('sin.pickle','rb') as sinsave:
    sin = pickle.load(sinsave)
with open('eud.pickle','rb') as eudsave:
    eud = pickle.load(eudsave)
with open('eudsq.pickle','rb') as eudsqsave:
    eudsq = pickle.load(eudsqsave)

# specify the intervals of words, windows to include
# the words come from: words_nonzero, not words any more
interval_words = raw_input('Specify the index intervals of words to include, within [0, %s], separated by semicolon: ' %str(len(words_nonzero)-1))
windows_toinclude = raw_input('Choose from windows %s, separated by comma: ' %str(windows)).split(',')

# specify weighting of each window
weights = map(float, raw_input('Specify weighting for each window, separated by comma: ').split(','))

# convert intervals into indices pointing to corresponding lists or dictionaries
indices_words = parseinterval(interval_words)

# parse windows values back to relative positions, that is, -2:0, -1:1...
indices_windows = []
for window in windows_toinclude:
    t = int(window)
    if t < 0:
        indices_windows.append(t+2)
    else:
        indices_windows.append(t+1)

# create sublists from indices: a list of words, and a list of their corresponding indices in words_nonzero
words_toinclude = []
indices_toinclude = []
for index_words in indices_words:
    i = index_words[0]
    while i <= index_words[1]:
        words_toinclude.append(words_nonzero[i])
        indices_toinclude.append(i)
        i += 1

# calculate the weighted cosine, sine, Euclidean distance and Euclidean distance squared
cos_weighted = {}
sin_weighted = {}
eud_weighted = {}
eudsq_weighted = {}
eud_b_weighted = {}
for word in words_toinclude:
    cos_weighted[word] = []
    sin_weighted[word] = []
    eud_weighted[word] = []
    eudsq_weighted[word] = []
    eud_b_weighted[word] = []
    for i in indices_toinclude:
        cos_raw = []
        sin_raw = []
        eud_raw = []
        eudsq_raw = []
        for window in indices_windows:
            cos_raw.append(cos[word][window][i])
            sin_raw.append(sin[word][window][i])
            eud_raw.append(eud[word][window][i])
            eudsq_raw.append(eud[word][window][i])
        cos_pikapika = weightedavg(cos_raw, weights)
        sin_pikapika = weightedavg(sin_raw, weights)
        eud_pikapika = weightedavg(eud_raw, weights)
        eudsq_pikapika = weightedavg(eudsq_raw, weights)
        if cos_pikapika > 1.0:
            cos_pikapika = 1
        elif cos_pikapika < 0.00001:
            cos_pikapika = 0
        if sin_pikapika > 1.0:
            sin_pikapika = 1
        elif sin_pikapika < 0.00001:
            sin_pikapika = 0
        if eud_pikapika > math.sqrt(2):
            eud_pikapika = math.sqrt(2)
        elif eud_pikapika < 0.00001:
            eud_pikapika = 0
        if eudsq_pikapika > math.sqrt(2):
            eudsq_pikapika = math.sqrt(2)
        elif eudsq_pikapika < 0.00001:
            eudsq_pikapika = 0
        cos_weighted[word].append(cos_pikapika)
        sin_weighted[word].append(sin_pikapika)
        eud_weighted[word].append(eud_pikapika)
        eudsq_weighted[word].append(eudsq_pikapika)
        eud_b_weighted[word].append(math.sqrt(eudsq_pikapika))

# write to csv
with open('cos_weighted.csv','wb') as cos_weightedsave:
    writer = csv.writer(cos_weightedsave, dialect = 'excel')
    writer.writerow(words_toinclude)
    for word in words_toinclude:
        writer.writerow(cos_weighted[word])
with open('sin_weighted.csv','wb') as sin_weightedsave:
    writer = csv.writer(sin_weightedsave, dialect = 'excel')
    writer.writerow(words_toinclude)
    for word in words_toinclude:
        writer.writerow(sin_weighted[word])
with open('eud_weighted.csv','wb') as eud_weightedsave:
    writer = csv.writer(eud_weightedsave, dialect = 'excel')
    writer.writerow(words_toinclude)
    for word in words_toinclude:
        writer.writerow(eud_weighted[word])
with open('eudsq_weighted.csv','wb') as eudsq_weightedsave:
    writer = csv.writer(eudsq_weightedsave, dialect = 'excel')
    writer.writerow(words_toinclude)
    for word in words_toinclude:
        writer.writerow(eudsq_weighted[word])
with open('eud_b_weighted.csv','wb') as eud_b_weightedsave:
    writer = csv.writer(eud_b_weightedsave, dialect = 'excel')
    writer.writerow(words_toinclude)
    for word in words_toinclude:
        writer.writerow(eud_b_weighted[word])