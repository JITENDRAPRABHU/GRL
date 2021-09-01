from decorators.do_thrice import do_thrice

@do_thrice
def call_do_thrice():
    print("Hello")

call_do_thrice()