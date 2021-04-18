
def avgWordsLength(sentence):

    wordList=sentence.split()
    return round(sum(len(w) for w in wordList)/len(wordList),2)


print(avgWordsLength('aaaa iiim ammm moha'))