#1  05-01-2021

d = {}
print(type(d))

d[1234] = 'celin'
d[1235] = 'Ilangoven'
d[1236] = 'Ilangoven'

print(d)

d = {1234:'celin',1235:'Ilangoven', 1236:'Rajarajan', 1237:'lenin'}
print(d)

#print(d[123])#key error

print(d[1236])
print(d[1234]) 
d[1234] = 'hari'
print(d)
d[100] = 'siva'
print(d)

#delete hari

del d[1235]

print(d)

#clear
#d.clear()
#print(d)

#del

#del d
#print(d)#not define

#lenth

print(len(d))
#get
print(d[1234])
print(d.get(1234))
print(d.get(12345))
#print(d.(12345))

#pop
#print(d.pop(1234))
#print(d)

#popitem
print("Before popitem ", d)
print(d.popitem())

print("After popitem ", d,) 


