def binary(no):
    binary = 0
    place = 1
    while no > 0:
        rem = no %2
        binary =binary + rem *place
        place = place * 10
        no = no // 2
    return binary
def main():
    
    num = int(input("enter the number"))

    ret = binary(num)

    print("binary number is ", ret)


if __name__ == "__main__":
    main()


