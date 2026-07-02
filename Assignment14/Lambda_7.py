def Divisible(no):
    return no % 5 == 0
def main():
    
    num = int(input("enter the first number :"))
    
    ret =Divisible(num)


    if ret:
        print(ret)
    else:
        print(ret)


if __name__ == "__main__":
    main()
