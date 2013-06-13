#!/usr/bin/python3
def remove_duplicates(sequence):
    newSequence = list(sequence)
    for element in newSequence:
        duplicates = newSequence.count(element) - 1
        if duplicates >= 1:
            for i in range(duplicates):
                newSequence.remove(element)
    return newSequence

