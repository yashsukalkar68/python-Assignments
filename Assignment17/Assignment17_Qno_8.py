def Pattern(no):
    for i in range(1,no+2):
        for j in range(1,i):
            print(j,end =" ")
        print()
       
def main():

    num = int(input("enter the number"))

    Pattern(num)
     
if __name__ == "__main__":
    main()
