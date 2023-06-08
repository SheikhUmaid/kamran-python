from random import randint 

a=randint(0,10)
while(True):
    b=int(input("enter num"))
    if b==a:
        print('you won')
        break
    else:
        print("try again")