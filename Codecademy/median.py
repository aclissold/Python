#!/usr/bin/python3
def median(unsortedNumList):
    numList = sorted(unsortedNumList)
    middle = len(numList) // 2
    if len(numList) % 2 != 0:
        medianValue = numList[middle]
    else:
        medianValue = (numList[middle-1] + numList[middle]) / 2
    return medianValue

if __name__ == '__main__':
    print(median([4, 5, 5, 4]))
