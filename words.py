#No. of words present in a sentence
sentence = 'today is wednesday'
wordsCount = 1 
for letter in sentence:
    if letter == ' ':
        wordsCount+=1
        print(letter, end=' ')
else:
    print('No. of words are ', wordsCount)


