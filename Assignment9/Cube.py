def Cube(no):
    no = no * no * no
    return no

def main():
    a=int(input("enter the number :"))
    ret = Cube(a)
    print("Cube is :",ret)

if __name__ == "__main__":
    main()