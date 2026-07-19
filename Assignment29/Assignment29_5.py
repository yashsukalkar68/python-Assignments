import sys
def main():

    if (len(sys.argv) < 3):
        print("insufficient number of arguuments :")
        return
    
    FileNmae = sys.argv[1]
    Str = sys.argv[2]

    fobj = open(FileNmae,"r")
    data = fobj.read()
    Count = data.count(Str)
    if Count > 0:
        print("String is present is file")
        print("count =",Count)
        
    else:
        print("not present ")

    fobj.close()


if __name__ == "__main__":
    main()