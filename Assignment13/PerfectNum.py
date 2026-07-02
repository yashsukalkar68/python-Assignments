def CheckPerfect(no):
    total=0
    for i in range(1,no):
        if no % i == 0:
            total=total+i
    if total == no:
        return True
    else:
        return False
        
def main():
    print("enter the number")
    a =int(input())
    
    ret = CheckPerfect(a)
    if ret:
        print("its a perfect num")
    else:
        print("its not a perfect num")


    

if __name__ == "__main__":
    main()
