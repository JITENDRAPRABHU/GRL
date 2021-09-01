def new_decor(func):
    def wrapper():
        func()
        func()
    return wrapper

@new_decor
def call_new_decor():
    print("HelloM WorlMd")

if __name__=="__main__":
    call_new_decor()