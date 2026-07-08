def Add(no1,no2):
    ans = no1+no2   

    return ans

def main():
    a = int(input("enter the number : - "))
    b = int(input("enter the number : - "))

    ret = Add(a,b)
    print("Addition is :-",ret)
    
if __name__ == "__main__":
    main()
