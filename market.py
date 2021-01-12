class SuperMarket:
    '''This is my supermarket''' #documentation string
    manufacturer = 'Muthu Supermarket'
    marketer = 'MSM'
    def __init__(self,x, y, z=None):#formal parameters
        self.brand = x
        self.price = y
        self.discount = z
        print("Check me Check me check me")

#self

bread = SuperMarket("ABC", 25, 25) #actual parameters
print(bread.brand)
biscuit = SuperMarket("PQR", 10.50, 25)
shampoo = SuperMarket("XYZ", 5, 25)

rice = SuperMarket("Seeragachamba", 65) #actual : 2
print(rice.discount)
print(SuperMarket.manufacturer)
print(SuperMarket.marketer)

#__init__ - is called automatically when the object is created 
