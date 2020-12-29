#numbers --> Iteration 
#Iteration--> looping
#looping --> while, for
# condition
# length 

mailid = input("Enter your mail id")
i =0 
while i<len(mailid):
    if not mailid[i]>='0' and mailid[i]<='9':
        if not mailid[i]>='a' and mailid[i]<='z':
            print(mailid[i], end=' ')
    i+=1 
