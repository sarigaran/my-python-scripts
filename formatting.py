#Formatting Strings: 
name = 'Raja'
salary = 20000
age = 55

print(name, salary, age)

print("{} is his name, his salary is {} and his age is {}".format(name, salary, age))
print("{0} is his name, his salary is {1} and his age is {2}".format(name, salary, age)) 

print("{a} is his name, his salary is {b} and his age is {c}".format(a=name,b=salary,c=age)) 
