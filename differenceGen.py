import numpy as np
import functools
import operator

def getStim(minLength,maxLength,numberOfTrials, allowIndentical):
    numberOfBins = 10
    
    xs = range(minLength, maxLength + 1)
    ys = range(minLength, maxLength + 1)
    # generate list of tuples containing all possible pairs and the difference for each pair
    pairs = list(map(lambda x: list(map(lambda y: (x, y, x - y if x > y else y - x), ys)), xs))

    # flatten list of pairs
    if allowIndentical:
        flatPairs = functools.reduce(operator.concat, pairs)
    else:
        # remove all pairs where x == y (i.e. both stimuli are the same)
        flatPairs = list(filter(lambda t: t[0] != t[1], functools.reduce(operator.concat, pairs)))
    # sort flat pairs by difference
    flatPairs.sort(key = lambda x: x[2])
    # list with only the differences from each possible pair (for sorting)
    differencesOnly = list(map(lambda q: q[2], flatPairs))

     # calculate min and max dif, and bin width
    maxDifference = max(differencesOnly)
    minDifference = min(differencesOnly)
    binWidth = (maxDifference - minDifference) / (numberOfBins)

    # list of the right sides of the bins
    delimiter = minDifference + binWidth
    binDelimiters = []
    for i in range(numberOfBins):
        if i == numberOfBins - 1:
            delimiter = maxDifference
        binDelimiters.append(delimiter)
        delimiter = delimiter + binWidth

    # list of the indices of the last instance of each bin
    indicesOfDelimiters = np.searchsorted(differencesOnly, binDelimiters, side = "right")

    # all the pairs, split into bins
    pairsSplitByBin = np.split(flatPairs, indicesOfDelimiters)[:-1]
    # from each bin, randomly sample some number (given by itemsPerBin) of indices for pairs in that bin 
    itemsPerBin = int(numberOfTrials / numberOfBins)
    # create empty stimulus set
    stimSet = []
    for x in pairsSplitByBin:
        indicesOfStimFromBin = np.random.choice(len(x), itemsPerBin, replace = False)
        # for each of those indices, get the stimulus pair and append to the stimulus set
        for index in indicesOfStimFromBin:
            stimSet.append(list(x[index]))
            
    return stimSet

if __name__ == "__main__":
    stim = getStim()
    print(len(stim))
    # print(stim)