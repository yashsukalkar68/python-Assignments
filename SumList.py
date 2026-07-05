from functools import reduce
AddList = lambda no1,no2: no1 + no2
def main():
    data =[10,20,30,40]

    print("input data :",data)

    Rdata = reduce(AddList,data)
    print("Addition of data is :",Rdata)

if __name__ == "__main__":
    main()