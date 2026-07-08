def CehckNum(no):
    if no >= 0:
        return True
    else:
        return False


def main():
    num = int(input("enter the number :- "))
    ret = CehckNum(num)

    if ret:
        print(f"{num} is positive number ")
    else:
        print(f"{num} is negative number ")

if __name__ == "__main__":
    main()
