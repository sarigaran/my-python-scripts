#while loop 
l = [10,7,5,3]
print('Before Sorting ', l)
j=1
while j<len(l):
    i= 0
    while i<len(l)-j: 
        if l[i]>l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
        i+=1
    j+=1

print('After sorting ', l) 
