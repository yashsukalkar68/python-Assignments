def CehckNum(no):
    if no % 5 == 0:
        return True
    else:
        return False


def main():
    num = int(input("enter the number :- "))
    ret = CehckNum(num)

    if ret:
        print(ret)
    else:
        print(ret)

if __name__ == "__main__":
    main()
