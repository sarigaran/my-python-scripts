prices = {'apple': 100, 'grapes': 200, 'banana': 50, 'orange': 60}

for prodName, prodPrice in prices.items():
    print(prodName, '--> ', prodPrice) 

#
for x in prices:
    print(x)
    
#    
    
prices = {'apple': 100, 'grapes': 200, 'banana': 50, 'orange': 60}

for prodName, prodPrice in prices.items():
    print(prices[prodName]) 
  #  
    (prices[prodName]) = (prices[prodName]) -10
print (prices)
