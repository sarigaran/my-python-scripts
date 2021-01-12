#1
#append operation


sentence = input("Enter a sentence: ") 
l1 = []  
for x in sentence: 
    l1.append(x) 
    l2 = []
    i = len(l1) - 1
    while i >= 0: 
        l2.append(l1[i])
        i -= 1 
        print(l2) 
        
#2      

#"Wish you a very happy New Year"
# 0 1 2 3 4 5 6
#Wish a happy year
sen = input("Enter a sentence ")
l = sen.split()
print(l)
l2=[]
i = 0 #3
while i<len(l):
    l2.append(l[i])#['d','c','b','a']
    #print(l[i], end=' ')
    i+=2 #i=2

print(l2) 



#3

#"Wish you a very happy New Year"
# 0 1 2 3 4 5 6
#Wish a happy year
sen = input("Enter a sentence ")
l = sen.split()
print(l)
l2=[]
i = 0 #3
while i<len(l):
    l2.append(l[i][::-1])#['d','c','b','a']
    #print(l[i], end=' ')
    i+=2 #i=2

print(l2)         




#4

#1) Get a sentence from User
#2) Convert that into a list l1
#3) Reverse the list l1 and store in another list l2
#4) Print list l2

#"Wish you a very happy New Year"
# 0 1 2 3 4 5 6
#Wish a happy year
sen = input("Enter a sentence ")
l = sen.split()
print(l)
l2=[]
i = 0 #3
while i<len(l):
    if i%2==0:
        l2.append(l[i][::-1])
    else:
        l2.append(l[i])
    i+=1 #i=2

print(l2) 



#5


sen = input("Enter a sentence ")
l = sen.split()
print(l)
l2=[]
i = 0 #3
while i<len(l):
    if i%2==0:
        l2.append(l[i][::-1])
    else:
        l2.append(l[i])
    i+=1 #i=2

print(l2) 
output = ''.join(l2)

print(output)

