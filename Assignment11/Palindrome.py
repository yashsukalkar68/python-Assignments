
def Palindrome(no):
    original = no
    reverse = 0
    while no > 0:
        digit = no %10
        reverse = reverse * 10 + digit

        no = no // 10
    if  original == reverse:
        return True
    else:
        return False        
def main():

    print("enter the number")
    a = int(input())
    ret = Palindrome(a)

    if ret:
        print("number is palindrome:")
    else:
        print("number is not  palindrome:")

if __name__ == "__main__":
    main()