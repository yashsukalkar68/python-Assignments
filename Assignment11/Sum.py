def CountDigit(no):
    Total=0
    while no > 0:
        digit = no % 10
        Total= Total + digit
        no = no // 10

    return Total
        
def main():

    print("enter the number")
    a = int(input())
    ret= CountDigit(a)
    print("sum is :",ret)


if __name__ == "__main__":
    main()
