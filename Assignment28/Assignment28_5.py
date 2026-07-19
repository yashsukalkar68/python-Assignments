def main():

    FileName =input("enter the file name to copy the data  :")
    word = input("enter the word that you want find in the file ")

    fobj = open(FileName,"r")
    data = fobj.read()

    if word in data:
        print("found")

    else: 
        print("not found")


    fobj.close()

if __name__ == "__main__":
    main()
