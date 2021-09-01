from decorators.my_decor import my_decor

@my_decor
def call_my_decor():
    print("Hello World")
    return call_my_decor
call_my_decor()
