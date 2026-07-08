import MarvellousNum
def ListPrime(data):
    total = 0
    for i in data:
        if (MarvellousNum.CheckPrime(i)):
            total = total + i
    return total
def main():
    data = []
    num = int(input("enter the number :-"))
    print("enter elements :-")
    for i in range(num):
        value =int(input())
        data.append(value)

        
    ret = ListPrime(data)
    print("list is :-",data)
    print("total is :",ret)
if __name__ == "__main__":
    main()