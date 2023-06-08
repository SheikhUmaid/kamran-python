import random
# print(a)
a=random.randint(0,10)
for i in range(50,100):
    user=int(input("enter num: "))
    if user==a:
        print("you won")
        break
    else:
        print("try again")

