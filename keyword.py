# types of argument
# 1.positional argument 
# 2.keyword argument
# 3.default argument
# 4.variable length argument

# keyword
def wish(name, msg):
    print('Hi', name, msg)

wish('Ganesh', 'Welcome')
wish(name='Ganesh', msg='Welcome')
wish(msg='Welcome',name='Ganesh') 


# 3.default argument

def wish(name='admin'):
    print('Hi',name)

wish()
wish('hari')

#ex 2 default
#def discount(perc = 10)
#discount(20)
#discount()

#ex 2 default
def calculateTotal(*n):
    total =0
    for subject in n:
        total = total + subject
    print(total)

calculateTotal(90)
calculateTotal(90,80,70)
calculateTotal() 
