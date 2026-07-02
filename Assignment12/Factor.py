def Factor(no):
    fact =[]
    for i in range(1,no+1):
        if no % i == 0:
            fact.append(i)

    return fact
def main():
    print("enter the number")
    a =int(input())
    
    ret = Factor(a)
    print("factorial is :",ret)

if __name__ == "__main__":
    main()