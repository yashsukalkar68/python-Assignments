SquareList = lambda no:no * no
def main():
    data = [1,2,3,4,5]

    print("input data is :",data)

    Mdata = list(map(SquareList,data))
    print("data after map :",Mdata)

if __name__ == "__main__":
    main()