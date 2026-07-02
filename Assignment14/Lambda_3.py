Max= lambda no1,no2: no1 > no2
def main():
    
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the  secound number :"))
    
    ret = Max(num1,num2)


    if ret:
        print("num1 is Max :",num1)
    else:
        print("num2  is Max:",num2)


if __name__ == "__main__":
    main()
