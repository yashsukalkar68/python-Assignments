def Arithmetic(no1,no2):
    Ans1 = no1 + no2
    Ans2 = no1 - no2
    Ans3 = no1 / no2
    Ans4 = no1 * no2
    return Ans1,Ans2,Ans3,Ans4
    

def main():
    print("enter the first number")
    num1 = int(input())
    print("enter the secound number")
    num2 = int(input())

    add,sub,div,mul=Arithmetic(num1,num2)
    
    print("Addition is ",add) 
    print("substraction is ",sub)
    print("Division is ",div)
    print("multiplication is ",mul)
    
    

if __name__ =="__main__":
    main()
