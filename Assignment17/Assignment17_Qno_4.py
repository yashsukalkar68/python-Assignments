def AdditionOfFactors(no):
    Sum = 0
    for i in range(1,no):
        if no % i == 0:
            Sum = Sum + i
    return Sum

def main():
    num= int(input("enter the number :- "))
    ret = AdditionOfFactors(num)
    print(ret)

if __name__ == "__main__":
    main()
