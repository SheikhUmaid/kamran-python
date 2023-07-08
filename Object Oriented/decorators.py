

def decorate(func):
    def mf():
        print("********")
        a = func()
        print("********")
        return a/2
    return mf

decorate(hello)()
@decorate
def hello():
    print("Hello! world")
    return 700

@decorate
def hello():
    print("Hello! world")
    return 700
def hello():
    print("Hello! world")
    return 700
def hello():
    print("Hello! world")
    return 700
def hello():
    print("Hello! world")
    return 700
def hello():
    print("Hello! world")
    return 700
def hello():
    print("Hello! world")
    return 700

print(hello())

