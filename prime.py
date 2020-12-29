#Prime No. 
no = int(input("Enter any number ")) #15
if no==2:
    print("prime")
else:
    for i in range(2,no): #2, 14
        if no%i==0:
            print('Not Prime')
            break 
    else:
        print("prime")
        #2 3 5 7 13 17 19
