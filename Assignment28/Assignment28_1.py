def main():

    FileName =input("enter the file name : ")
    fobj=open(FileName,"r")

    count = 0
    for lines in fobj:
        count = count +1    
    fobj.close()
    print("total numbers of line :-",count)

if __name__ == "__main__":
    main()
