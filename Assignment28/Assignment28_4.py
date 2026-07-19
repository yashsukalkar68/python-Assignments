def main():

    FileName1 =input("enter the file name to copy the data  :")

    fobj1 = open(FileName1,"r")
    data = fobj1.read()
    fobj1.close()
   
    FileName2 =input("enter the file name to paste the data   :")

    fobj2 = open(FileName2,"w")
    data = fobj2.write(data)
    fobj2.close()


    print(f"content of {FileName1} is copied and pasted in {FileName2} sucessfully")

 

if __name__ == "__main__":
    main()
