from __future__ import division
import math
# concatenate a list of vectors into one vector
def concatenate(listofvectors):
    vector_conc = []
    for vector in listofvectors:
        vector_conc += vector
    return(vector_conc)

# first normailse all vectors, then the cosine similarity is simply the dot product
# normalise a vector to a unit vector
def normalise(vector):
    magsqr = 0
    for num in vector:
        magsqr += num**2
    magnitude = math.sqrt(magsqr)
    vector_norm = []
    if magnitude == 0:
        return ([0]*len(vector))
    else:
        for num in vector:
            num_norm = num/magnitude
            vector_norm.append(num_norm)
        return(vector_norm)

# check if a vector is zero
def zerovect(vector):
    return all(num is 0 for num in vector)

# calculate dotprodoct of two vectors  
def dot(vector1, vector2):
    dotproduct = 0
    for i in range(len(vector1)):
        dotproduct += vector1[i] * vector2[i]
    return dotproduct

# ZeroDivisionError doesn't work with numpy, so write an if version
def invert(value):
    if value == 0:
        return 9999
    else:
        return (1/value)
    
# generate regex pattern
def regexgen(core, number, periph):
    if number < 0:
        regex = periph + '\\W+\\w+'*(abs(number)-1) + '\\W+' + core
    else:
        regex = core + '\\W+\\w+'*(number-1) + '\\W+' + periph
    return regex

# interval parser; takes a string and parses it into a list of lists of two integers as indices
def parseinterval(interval):
    indices = []
    sections = interval.split(';')
    for i, section in enumerate(sections):
        indices.append([])
        borders = section.split(',')
        if borders[0].startswith('['):
            indices[i].append(int(borders[0][1:]))
        else:
            indices[i].append(int(borders[0][1:])+1)
        if borders[1].endswith(']'):
            indices[i].append(int(borders[1][:-1]))
        else:
            indices[i].append(int(borders[1][:-1])-1)
    return indices

# weight a list against another list
def weightedavg(raw, weighting):
    weighted = 0
    for i in range(len(raw)):
        weighted += raw[i] * weighting[i]
    return weighted

# merge two dstr entries into one; in specific, the entries are two equal-length lists of equal-length lists; to merge is to add the lowest-level list elements up
def merge(x,y):
    z = []
    for m in range(len(x)):
        z.append([])
        for n in range(len(x[0])):
            z[m].append(x[m][n]+y[m][n])
    return z

# calculate the squared Euclidean distance between two vectors
def euclideansq(u,v):
    eudsq = 0
    for i in range(len(u)):
        eudsq += (u[i]-v[i])**2
    return eudsq