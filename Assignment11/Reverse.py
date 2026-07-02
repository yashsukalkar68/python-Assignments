
def Reverse(no):
    reverse =0
    while no > 0:
        digit = no %10
        reverse = reverse * 10 + digit

        no = no // 10
    return reverse
    
        
def main():
    print("enter the number :")
    a=int(input())

    ret = Reverse(a)
    print("reverse number is :",ret)

if __name__ == "__main__":
    main()