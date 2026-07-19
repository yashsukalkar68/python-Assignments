import sys
def main():

    if (len(sys.argv) < 2):
        print("insufficient number of arguuments :")
        return
    
    File1 = sys.argv[1]
    File2 = sys.argv[2]

    Fobj1 = open(File1,"r")
    Fobj2 = open(File2,"r")
    
    
    data1 = Fobj1.read()
    data2 = Fobj2.read()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

    Fobj1.close()
    Fobj2.close()
    
    
    
    
if __name__ == "__main__":
    main()