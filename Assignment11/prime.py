def CheckPrime(no):
    if no <= 1:
        return False
    for i in range(2,no):
        if no % i ==0:
            return False
    return True    
 
def main():
    print("enter the number")
    a = int(input())

    if CheckPrime(a):
        print("number is prime",a)
    else:
        print("number is not prime",a)

  

if __name__ == "__main__":
    main()