mind = 45
guess = 0
while guess!=mind:
    guess = int (input("tell me your guess"))
if guess == mind:
    print("wow supere")
elif guess>mind:
    print("no,your guess is grester")
else:
    print("no,too little")
