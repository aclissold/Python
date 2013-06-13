#!/usr/bin/python3
def censor(text, censorWord):
    sentence = ''               # Used to recombine wordList
    wordList = text.split(" ")  # Make a List of words
    for index, word in enumerate(wordList):
        if word == censorWord:
            word = '*' * len(word)  # Replace words that should be censored
            wordList[index] = word
    for word in wordList:
        sentence += word + ' '
    sentence = sentence.strip()
    return sentence

if __name__ == '__main__':
    print(censor("hey hey hey", "hey"))
