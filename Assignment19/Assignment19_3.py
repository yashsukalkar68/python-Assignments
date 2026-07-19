from functools import reduce
ChckNum = lambda num: num >= 70 and num <=90
Increment = lambda num: num + 10
Addition  = lambda no1,no2 : no1*no2

def main():
    data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Input Data is : ",data)

    fdata = list(filter(ChckNum,data))
    print("data after filter:-",fdata)

    mdata = list(map(Increment,fdata))
    print("data after map :-",mdata)

    rdata = reduce(Addition,mdata)
    print("dta afte reduce:-",rdata)

if __name__ == "__main__":
    main()
