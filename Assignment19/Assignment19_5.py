from functools import reduce
def Prime(no):
    if no <= 1:
        return False 
    for i in range(2,no):
        if no % i == 0:
            return False
    return True 
def Mult(no):
    return no * 2
def Max(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2 

def main():
    
    data = []
    num = int(input("enter the numbers of elements :-"))
    print("enter elements :-")
    for i in range(num):
        value = int(input())
        data.append(value)

    fdata =list(filter(Prime,data))
    print("data after filter is :-",fdata)

    mdata = list(map(Mult,fdata))
    print("data after map is :-",mdata)

    rdata = reduce(Max,mdata)
    print("data after reduce is :-",rdata)


if __name__ =="__main__":
    main()

