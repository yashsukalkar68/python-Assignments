def Number(no):
    str=[]
    for i in range(1,no+1):
        str.append(i)
    return str

def main():
    print("enter the number")
    num = int(input())

    ret =Number(num)
    print("numbers :",ret)



if __name__ =="__main__":
    main()
