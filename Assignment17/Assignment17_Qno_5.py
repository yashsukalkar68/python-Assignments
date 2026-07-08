def ChckPrime(no):
    if no <=1:
        return False
    for i in range(2,no):
        if no % i == 0:
            return False
    return True 
        

def main():
    num= int(input("enter the number :- "))
    ret = ChckPrime(num)
    if ret:
        print("it is prime")
    else:
        print("not prime")

if __name__ == "__main__":
    main()
