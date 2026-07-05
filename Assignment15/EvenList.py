EvenList = lambda no:no % 2  == 0
def main():
    data = [10,21,32,43,15]

    print("input data is :",data)

    Fdata = list(filter(EvenList,data))
    print("data after filter :",Fdata)
    
if __name__ == "__main__":
    main()