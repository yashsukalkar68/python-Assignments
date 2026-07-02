def Square(no):
    no = no * no
    return no

def main():
    a=int(input("enter the number :"))
    ret = Square(a)
    print("square is :",ret)

if __name__ == "__main__":
    main()