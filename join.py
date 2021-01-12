#input: Sun Mon Tues Wednes Thurs Fri Satur
#output: Sunday Monday Tuesday Wednesday Thursday Friday Saturday

input = 'Sun Mon Tues Wednes Thurs Fri Satur'
words = input.split()
words2=[]
for word in words:
    if word[-1]=='s':
     #if len (words)>=4
            words2.append(word+'day')

#print(words2)

output = ', '.join(words2)

print(output) 
