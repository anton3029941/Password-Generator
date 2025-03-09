import random
symbols = "qwertyuiop1234567890asdfghjklzxcvbnm._QWERTYUIOPASDFGHJKLZXCVBNM"
symbols = list(symbols)
false = True
while false:
    length = input("Length of password: ")
    try:
        int(length)
        break
    except:
        print("Try again")
password = ""
for i in range(int(length)):
    password += symbols[random.randint(0, len(symbols))]
print(password)
