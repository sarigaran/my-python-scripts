def odd_even(no):#no=5
    if no%2==0:
        print('Even')
    else:
        print('Odd')
#num = int(input("Enter no. ")) 
odd_even(90) 


#calculator

def calculate(no1, no2):
    add = no1 + no2
    sub = no1 - no2
    mul = no1 * no2
    div = no1 // no2
    return add, sub, mul, div


result = (calculate(100,50)) 
print(result)
print(type(result))
for x in result:
    print(x)


    
    





