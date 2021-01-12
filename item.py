employees = {'Kathiravan':25000, 'Viyan': 30000, 'Navilan': 40000, 'Arul':18000}

for name, salary in employees.items():
    if salary>25000:
        print(name, ' salary is ', salary) 
    
    
    
nameList = [] 
for name in employees.keys():
    nameList.append(name) 
print(nameList) 
