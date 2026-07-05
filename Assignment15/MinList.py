from functools import reduce
Min = lambda no1,no2 :no1 if no1 < no2  else no2 
def main():
    
    data = [10,2,11,45]

    print("input data :",data)

    rdata = reduce(Min,data)

    print("Min is :",rdata)
if __name__ == "__main__":
    main()
