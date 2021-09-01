def decor_1(func):
    def wrap():
        x=func()
        return x*x
    return wrap

def decor(func):
    def wrap():
        x=func()
        return 2*x
    return wrap
    
@decor_1
@decor
def pro():
    return 10



print(pro())