def CountDigit(no):
    digit = 0
    while no > 0:
        no = no // 10
        digit = digit + 1
    return digit
       
def main():

    num = int(input("enter the number"))

    ret = CountDigit(num)
    print(ret)
if __name__ == "__main__":
    main()
