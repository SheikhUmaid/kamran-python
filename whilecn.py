from random import randint
a=randint(0,10)
chances=3
while True:
    print(f'{chances} chances left!')
    if chances <= 0:
        print('you lose')
        break
    user=int(input("enter no: "))
    if user < a:
        print('more')
        chances -= 1 # chances = chances - 1
    elif user > a:
        print('less')
        chances -= 1 # chances = chances - 1
    elif user == a:
        print("you won")
        break
    else:
        print('enter right no')