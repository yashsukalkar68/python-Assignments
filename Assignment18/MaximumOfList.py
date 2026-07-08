def Max(data):
    Maximum = data[0]

    for i in data:
        if i > Maximum:
            Maximum = i
    return Maximum
def main():

    data = []
    num = int(input("enter the number"))
    print("enter the elements")
    for i in range(num):
        value = int(input())
        data.append(value)
    
    ret = Max(data)
    
    print("entered List is :",data)
    print("Maximum is ",ret)


if __name__ == "__main__":
    main()