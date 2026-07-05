def CountEven(no):
    return no % 2 == 0
def main():
    data = [10,21,32,43,15]

    print("input data is :",data)

    Fdata = len(list(filter(CountEven,data)))
    print("data after filter :",Fdata)
    
if __name__ == "__main__":
    main()