def censor(text, censorWord):
    sentence = ''               # Used to recombine wordList
    wordList = text.split(" ")  # Make a List of words
    for word in wordList:
        if word == censorWord:
            word = '*' * len(word)  # Replace words that should be censored
            print word
    for word in wordList:
        sentence += word + ' '
    sentence = sentence.strip()
    return sentence
