from functools import reduce

def Even(no):
    return no % 2 == 0
def Square(no):
    return no * no
def Add(no1,no2):
    return no1 + no2
def main():
    data =[5,2,3,4,3,4,1,2,8,10]
    print("input list is :-",data)

    fdata = list(filter(Even,data))
    print("data after filter is :- ",data)

    mdata = list(map(Square,fdata))
    print("data after map is :-",mdata)

    rdata = reduce(Add,mdata)
    print("data after reduce is : -",rdata)


if __name__ == "__main__":
    main()