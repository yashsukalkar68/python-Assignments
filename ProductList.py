from functools import reduce
def Product(no1,no2):
    return no1*no2
def main():


    data = [2,3,4,5]

    rdata = reduce(Product,data)

    print("product of data is :",rdata)


if __name__ == "__main__":
    main()