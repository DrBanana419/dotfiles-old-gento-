#sample lyrics list
richie=['looking', 'it', 'Hello', 'is', 'it', 'me', 'you', 'are', 'looking', 'for', 'I', 'can', 'see', 'it']

#function for converting list into a dictionary

def num_words(lyrics):
    fd={}
    for word in lyrics:
        if word in fd:
            fd[word]=fd[word]+1
        else:
            fd[word]=1
    return fd

#function for finding the most frequent word

def most_common_words(dictionary):
    values=list(dictionary.values())
    best=max(values)
    words=[]
    for key in dictionary:
        if dictionary[key]==best:
            words.append(key)

    return (words, best)

dictrichie=num_words(richie)
print(most_common_words(dictrichie))
def words_often(freqs, mintimes):
    result=[]
    done = False
    while not done:
        temp=most_common_words(freqs)
        if temp[1] >= mintimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True

    return result

print(words_often(dictrichie, 2))
