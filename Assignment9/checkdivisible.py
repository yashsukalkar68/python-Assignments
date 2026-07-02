def CheckDivisible(no):
    if (no %3 == 0) and (no % 5 == 0):
        return True
    else:
        return False
def main():
    a = int(input("enter the number :"))

    ret=CheckDivisible(a)

    if ret:
        print("number is divisible by 3 and 5")
    else:
        print("not divisible by 3 and 5")

if __name__ =="__main__":
    main()
