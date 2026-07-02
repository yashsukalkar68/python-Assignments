def Natural(no):
    total = 0
    for i in range(1,no+1):
        print(i)
        total = total +i
    return total
    
def main():
    
    a = int(input("enter the number"))
    ret = Natural(a)
    print("Total is :",ret)

if __name__ == "__main__":
    main()