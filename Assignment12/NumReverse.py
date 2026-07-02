def NumberRev(no):
    str=[]
    for i in  range(no,0,-1):
       str.append(i)
    return str



def main():
    print("enter the number")
    num = int(input())

    ret =NumberRev(num)
    print("Reverse number is :",ret)


if __name__ =="__main__":
    main()
