def Pattern():
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end =" ")
        print()
def main():
        Pattern() 

if __name__ == "__main__":
    main()
