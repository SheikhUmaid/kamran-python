from brute import login




for i in range(999,10000):
    a=login(i)

    if a==True:
        print(f'password is {i}')
        break
    else:
        print('checking again')