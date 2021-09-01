def histogram(n):
    for i in range(len(n)):
        for j in range(n[i]):
            print("*",end='')
        print()
histogram([2,3,6,5])