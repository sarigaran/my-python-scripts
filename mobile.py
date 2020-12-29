mobile = '1234567890'
#print(s.startswith('python'))
#print(s.endswith('python'))

for letter in mobile:
    if not (letter>='0' and letter<='9'):
        print('Not correct mobile number')
        break
else:
    print("Correct Mobile Number") 
