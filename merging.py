#merging letters

s1 = 'pto'
s2 = 'yhn'

#output = s1[0] + s2[0] + s1[1] + s2[1] + s1[2] + s2[2]


output=''
i=0
while i<len(s1):
    output = output+s1[i] #'p''t''o'
    output = output+s2[i] #'y''h''n'
    i+=1
else:
    print(output) 
