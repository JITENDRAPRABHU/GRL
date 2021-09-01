def recursive_list_sum(num):
    sum=0
    for i in num:
        if(type(i)==type([])):
            sum+=recursive_list_sum(i)
        else:
            sum=sum+i
    return sum

if __name__ =="__main__":
    print(recursive_list_sum([1,2,3,[4,5,6],7,8,[9,10]]))
    print(recursive_list_sum([1,4,2,3,5,[9,7,6],7,1]))