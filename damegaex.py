import random
lie=["Do not frust.It almost near","Too big","Too low","Very close","Just a little","Come on, it's there","Bigger than that","Lower than that","Sooooo close","Far far away, try harder"]
print ("WELCOME TO THE GUESSING GAME.")
print ("I have 2 digits number in my mind and you have to guess it.")
print ("You have 10 tries and you may start guessing now.")
#uin=random.randint(5,9)
dr=random.randint(10,99)
n=0
while n<10:
    n=n+1
    usr1=input("Input your guess: ")
    if n<10:
        if dr==usr1:
            print("GOTCHA!!!The number is %d. SUPERB.") %(usr1)
            break
        else:
            print random.choice(lie)
    else:
        print("You FAIL!!!This is the number: %d") %(dr)