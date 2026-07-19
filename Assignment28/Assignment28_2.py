def main():

    FileName =input("enter the file name : ")
    fobj=open(FileName,"r")

    count = 0
    for lines in fobj:
        words = lines.split()
        count = count + len(words)    
    fobj.close()
    print("total numbers of words:-",count)

if __name__ == "__main__":
    main()
