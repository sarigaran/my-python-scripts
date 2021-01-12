
# sum of digits
#1873
def sumOfDigits(num):
    if num==0:
        return 0
    else:
        rem = num%10
        no = int(num/10)
        return rem + sumOfDigits(no) 
        #3 + sum(187) 10 + sum(18)

#print(sumOfDigits(1873)) 

num = int(input("enter your number"))
print("the sum of ",num,"is",sumOfDigits(num)) 


# 2 example :2

squareofnum = lambda num:num*num
print(squareofnum(5))


# ex :3
bigOfTwo = lambda no1, no2:no1 if no1>no2 else no2

print(bigOfTwo(10,20)) 

# ex: 4

sumOfTwo = lambda no1, no2:no1 + no2

print(sumOfTwo(10,20)) 








