
import random as rd
a=rd.randint(0,10)
b=rd.randint(0,10)
d=a*b
chances=3
while True:
    print(f"{chances} chances left")
    print(F'{a} X {b}= ')
    c=int(input('Enter solution: '))
    user=d
    if user==c:
        print('You won')
        break
    elif chances ==0:
        print('You lose')
        break
    else:
        print("You lose")
    chances -=1