def uppercase(a):
    def wrap():

        re=a()
        op=re.upper()    
        return op
    return wrap

def lowercase(a):
    def wrap():
        re=a()
        op=re.lower()
        return op
    return wrap

@uppercase
def greet():
    return 'hello world!'

@lowercase
def greetl():
    return 'HELLO!'

op=greet()
opl=greetl()
print(op)
print(opl)