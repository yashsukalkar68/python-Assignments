def ChckNum(no):
    if no % 2 == 1:
        return True
    else:
        return False

def main():
    a = int(input("enter the number : - "))
    ret = ChckNum(a)
    if ret:
        print("Odd number ")
    else:
        print("even Number")
if __name__ == "__main__":
    main()
