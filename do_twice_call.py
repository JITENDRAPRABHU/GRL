from decorators.do_twice import do_twice

@do_twice
def cal_do_twice():
    print("HI")

print(cal_do_twice())