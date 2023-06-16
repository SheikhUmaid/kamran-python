

def func():
    try:
        array = [1,2,3,4]
        a = input("enter index: ")
        print(array[int(a)])
        return 0
    except:
        print("something went wrong")
        return 1
    finally:
        print("Finalyy executed")


func()


def funct2():
    return 0
    print("something")
    print("something")
    print("something")
    print("something")
    print("something")
    print("something")
    print("something")

# funct2()