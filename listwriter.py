from __future__ import print_function
from mylibrary import regexgen

# get windows
windows = map(int, raw_input('Please specify windows left to right separated by comma: ').split(','))

# get weighting
# weights = map(float, raw_input('Please specify the weight of each window separated by comma: ').split(','))

# get words size & context, create words and contexts
fwdlist = open('wordlist.list')
wdlist = fwdlist.read().split()
fwdlist.close()
maxsize = len(wdlist)
wordssize = int(raw_input('Please specify the number of words to classify [3, %d]: ' %maxsize))
contextssize = int(raw_input('Please specify the number of contexts to consider [2, %d]: ' %maxsize))
words = wdlist[:wordssize]
contexts = wdlist[:contextssize]

# print a list of regex patterns, in this format: [[[word,j,k],'pattern'],...]
with open('lists.py','wb') as lists:
    print('words = ', words, file = lists)
    print('contexts = ', contexts, file = lists)
    print('windows = ', windows, file = lists)
    print('environments = [', file = lists)
    for i, word in enumerate(words):
        for j, window in enumerate(windows):
            for k, context in enumerate(contexts):
                print("[['%s', %d, %d],'%s']," %(word,j,k,regexgen(word,window,context)), file = lists)
    print(']', file = lists)