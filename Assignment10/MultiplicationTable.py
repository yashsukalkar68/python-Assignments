def Multiplication(no):
    for i in range(1,11):
        print(no*i)

def main():
    print("multiplication table:")
    a =int(input())

    ret =Multiplication(a)

if __name__ == "__main__":
    main()