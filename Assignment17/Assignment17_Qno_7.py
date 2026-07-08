def Pattern(no):
    for i in range(5):
        for j in range(1,5):
            print(j,end =" ")
        print()
       
def main():

    num = int(input("enter the number"))

    Pattern(num)
     
if __name__ == "__main__":
    main()
