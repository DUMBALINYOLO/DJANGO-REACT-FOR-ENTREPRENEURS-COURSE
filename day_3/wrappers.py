

# Modify the behavior of a function without modifying it permanently
# It wraps another function and since both functions are callable, it returns a callable


def function1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to DuMBA cLASSICS")
    return wrapper

@function1
def function2():
    print("Pythonista")

function2()


def func1(function):
    def wrapper(*zombie, **kwargs):
        # print("Hello")
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        # print("WELCOME Dumba Classics")
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
        function(*zombie, **kwargs) ## hahaha interesting any word can go for args or kwargs
    return wrapper

@func1
def func2(name):
    print(f"{name}")

func2("Dumbalinyolo")
func2("Baridzi")

def func1(func):
    def wrapper(*args, **kwargs):
        print("It worked")
        func(*args, **kwargs) #It calls arguments passed in a wrapped function
    return wrapper


@func1
def func2(name):
    print(f"{name}")


func2("Maximillem")
