OddList = lambda no : no % 2  == 1
def main():
    data = [10,21,32,43,15]

    print("input data is :",data)

    Fdata = list(filter(OddList,data))
    print(" odd number after filter :",Fdata)
    
if __name__ == "__main__":
    main()