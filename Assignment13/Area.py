def Area(length,width):
    Area=length * width
    return Area
def main():

    lth = int(input("enter the length :"))
    wdh = int(input("enter the width :"))

    ret = Area(lth,wdh)
    print("Area of rectrangle is :",ret)
if __name__ == "__main__":
    main()