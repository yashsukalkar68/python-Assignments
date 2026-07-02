def Odd(no):
    data=[]
    for i in range(1,no+1):
        if i % 2 == 1:
           data.append(i)
    return data
    
def main():
    print("enter the number")
    a =int(input())

   
    ret=Odd(a)
    print("Odd numbers are:",ret)

if __name__ == "__main__":
    main()