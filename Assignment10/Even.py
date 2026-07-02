def Even(no):
    data=[]
    for i in range(1,no+1):
        if i % 2 == 0:
           data.append(i)
    return data
    
def main():
    print("enter the number")
    a =int(input())

   
    ret=Even(a)
    print("Even numbers are:",ret)

if __name__ == "__main__":
    main()