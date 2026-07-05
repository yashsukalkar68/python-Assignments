from functools import reduce
Max = lambda no1,no2 :no1 if no1 > no2  else no2 
def main():
    
    data = [10,2,11,45]

    print("input data :",data)

    rdata = reduce(Max,data)

    print("Max is :",rdata)
if __name__ == "__main__":
    main()
