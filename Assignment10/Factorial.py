def Factorial(no):
    fact = 1
    for i in range(1,no+1):
   
        fact = fact * i
    return fact
def main():
    print("enter the number")
    a =int(input())
    
    ret = Factorial(a)
    print("factorial is :",ret)

if __name__ == "__main__":
    main()