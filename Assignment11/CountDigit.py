def CountDigit(no):
    count = 0
    while no > 0:
        no = no // 10
        count +=1
    return count
    
   # return len(str(no))

def main():
    print("enter the number")
    a = int(input())

    ret = CountDigit(a)
    print("count of Digit is:",ret)





if __name__ == "__main__":
    main()