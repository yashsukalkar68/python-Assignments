def main():
    FileName =input("enter the file name :")
    fobj = open(FileName,"r")

    for lines in fobj:
        print(lines,end = " ")
    
    fobj.close()

if __name__ == "__main__":
    main()
