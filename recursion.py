
#Recursion:

# cursive writing
#recursive

def getUserNamePassword(username, password):
    if username != 'abcd':
        print("Incorrect Username")
        username = input("Enter user name ")
        password = input("Enter password " )
        getUserNamePassword(username, password)

    elif password !='abcd':
        print("Incorrect Password")
        username = input("Enter user name ")
        password = input("Enter password " )
        getUserNamePassword(username, password)

username = input("Enter user name ")
password = input("Enter password " )

getUserNamePassword(username, password)


# 2 example 

#n = int(input("enter your number"))

def display(n):#formal argument

    print(n) #1 2
    n+=1 #3
    if n<=10:
        display(n) #display(2) display(3)


display(1) #actual argument 


# 3 example

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
result = fact(5)
print(result)
n=int(input("enter the number="))
print("the factorial of ",n,"is",fact(n)) 
fact(n)



