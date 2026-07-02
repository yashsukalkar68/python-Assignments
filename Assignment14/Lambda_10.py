Compare = lambda no1,no2,no3:no1 if no1 >= no2 and no1 >= no3 else no2 if no2 >= no1 and no2 >= no3 else no3
def main():
    
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the  secound number :"))
    num3 = int(input("enter the  third number :"))
    ret = Compare(num1,num2,num3)

    print("max is ",ret)

if __name__ == "__main__":
    main()
