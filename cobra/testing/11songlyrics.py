richie=['Hello', 'is', 'it', 'me', 'you', 'are', 'looking', 'for', 'I', 'can', 'see', 'it']
def num_words(lyrics):
    fd={}
    for word in lyrics:
        if word in fd:
            fd[word]=fd[word]+1
        else:
            fd[word]=1
    return fd

print(num_words(richie))

number_list=list(num_words(richie).values())
word_list=list(num_words(richie).keys())

print(number_list)

m=max(number_list)
position=number_list.index(m)
print(word_list[position], m)


