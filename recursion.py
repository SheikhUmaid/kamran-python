counter = 100
def toN(n):
    if n == counter:
        return True
    else:
        n+=1
        print(n)
        toN(n)
toN(10)


