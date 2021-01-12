# Binary Search:
#Suitable for sorted set of elements

l = [10,20,30,40,52,68,79,90]
# 0 1 2 3 4 5 6 7
key = int(input("Enter key to search ")) #1
min = 0 #min=0
max = len(l)-1 #max =7

while min<=max:
    avg = (min+max)//2 #avg = 0
    if key==l[avg]: #1=10
        print("key is present at ", avg)
        break
    elif key>l[avg]: #1>10
        min = avg + 1
    else:
        max = avg - 1 #max=-1
    #else:
        print('key is not present')










