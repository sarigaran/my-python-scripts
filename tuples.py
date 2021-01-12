

t = (10,20,30,40,50,60,70,80,90,100)


print(t[0])
print(t[-1])
print(t[1]) #IndexError


print(t[2:5])
print(t[::2])

#t[1] = 123 #TypeError 

t1 = (10,20,30)
t2 = (5,10,15)
t3 = t1+ t2
print(t3)
print("over")
##

print(len(t3))
print(t3.count(10))
print(t3.index(10))
t5 = sorted(t3)
print(t5)
print(max(t5))
print(min(t5))
print(sum(t5))

t4 = t1*2
print(t4) 




#Tuple Comprehension

t = (i**i for i in range(1,6))

print(type(t))

for value in t:
    print(value) 




###
t= eval(input("Enter values : "))
print(t) 
for x in t:
    print(x) 

