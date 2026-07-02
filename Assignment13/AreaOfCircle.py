def AreaOfCircle(r):
    pi=3.14
    Area = pi* r * r
    return Area
def main():

    Radius = int(input("enter the Radius :"))
    ret = AreaOfCircle(Radius)
    print("Area of circle is :",ret)
if __name__ == "__main__":
    main()