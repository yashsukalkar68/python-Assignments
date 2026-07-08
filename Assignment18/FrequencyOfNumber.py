def Frequency(data,no):
    Count = 0
    for i in data:
        if i == no:
            Count = Count + 1
    return Count
def main():

    data = []
    num = int(input("enter the number"))
    print("enter the elements")
    for i in range(num):
        value = int(input())
        data.append(value)

    find = int(input("enter the number you want to find the frequency :-"))
    ret = Frequency(data,find)

    print("entered List is :",data)
    print("frequency of no is",ret)


if __name__ == "__main__":
    main()