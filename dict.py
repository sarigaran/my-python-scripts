#d = eval(input("enter dictionary"))
#print(d)


#Getting items for dictionary at run time
register = {}
#no = int(input("Enter no. of students "))
#i = 1
while True:#i<=no:
    name = input("Enter name ")
    mark = int(input("Enter mark "))
    register[name] = mark
    nextcandidate  = input("enter No to stop")
    if nextcandidate=='No':
        break 
     
    #no+=1 
    
