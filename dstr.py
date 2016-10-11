import regex as re, os, cPickle as pickle
from lists import words, contexts, windows, environments

# get list of text file names in the Corpus subdirectory
li_filename = []
rel_path = 'Corpus/'
abs_path = './Corpus/'
for filename in os.listdir(abs_path):
    if filename.endswith('.txt'):
        li_filename.append(rel_path+filename)

# # small range test corpus
# li_filename = []
# rel_path = 'testcorpus/'
# abs_path = './testcorpus/'
# for filename in os.listdir(abs_path):
#     if filename.endswith('.txt'):
#         li_filename.append(rel_path+filename)

# initiate dictionary to store distributions
dstr = {word:[[0 for context in contexts] for window in windows] for word in words}

# compile regex patterns to regex objects
reobjs = []
for index, regex in environments:
    reobjs.append([index, re.compile(r'\b%s\b' %regex, re.IGNORECASE)])

# read in text file, cut to sentences, count frequency, put in dictionary
for filename in li_filename:
    with open(filename,'rb') as fileread:
        sentences = filter(None, re.split(r'\n|\.|\?|!|;', fileread.read()))
    for sentence in sentences:
        for index, reobj in reobjs:
            word, j, k = index
            dstr[word][j][k] += len(reobj.findall(sentence, overlapped = True)) # speed up this process by only counting half of them; this only works with the overlapping part between words and contexts

# store distribution in a file
with open ('dstr.pickle', 'wb') as dstrsave:
    pickle.dump(dstr, dstrsave)