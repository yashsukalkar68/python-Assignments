def checkGreater(no1,no2):
    return no1 >no2
    return no2 >no1

def main():
    
        value1=int(input("enter first number"))
        value2=int(input("enter secound number"))
        
        if value1 == True:
            ret = checkGreater(value1,value2)
            
            print("greater number is ",value1)
        else:
            print("greater number is :",value2)
    

if __name__ == "__main__":
    main()