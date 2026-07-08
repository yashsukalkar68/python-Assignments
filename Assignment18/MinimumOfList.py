def Min(data):
    Min = data[0]
    for i in data:
        if i < Min:
            Min = i
    return Min
def main():

    data = []
    num = int(input("enter the number"))
    print("enter the elements")
    for i in range(num):
        value = int(input())
        data.append(value)
    
    ret = Min(data)
    
    print("entered List is :",data)
    print("Minimum is ",ret)


if __name__ == "__main__":
    main()