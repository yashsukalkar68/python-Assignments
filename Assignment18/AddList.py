def AddirtionofElements(data):
    total=0
    for i in data:
        total = total + i
    return total
def main():
    data = []
    num = int(input("enter the number of elements :"))
    print("enter the numberss :")
    for i in range(num):
        value=int(input())
        data.append(value)

    ret = AddirtionofElements(data)
    print("List is :",data)
    print("addition  of elements is:",ret)

if __name__ == "__main__":
    main()