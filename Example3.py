def printUnorderedPairs(array):

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print(array[i] + "," + array[j])
