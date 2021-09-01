def decor(func):
    def wrap():
        print("Before func")
        print(func())
        print("After Func")
        
    return wrap

@decor
def say_hi():
    return "HI....!"

say_hi()
