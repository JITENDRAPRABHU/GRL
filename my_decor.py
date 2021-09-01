def my_decor(func):
    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")
    return wrapper