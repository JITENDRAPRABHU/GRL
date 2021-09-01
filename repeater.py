#import time
def repeat(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat
def repeat_call():
    print( "repeated")
repeat_call()