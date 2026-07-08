def SumDigit(no):
    digit = 0
    TotalNo = 0
    while no > 0:
        digit = no % 10
        TotalNo = TotalNo + digit
        no = no // 10

    return TotalNo
       
def main():

    num = int(input("enter the number"))

    ret = SumDigit(num)
    print(ret)
if __name__ == "__main__":
    main()
