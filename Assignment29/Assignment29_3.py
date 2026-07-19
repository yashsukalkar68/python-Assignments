import sys
def main():

    if (len(sys.argv) < 3):
        print("insufficient number of arguuments :")
        return
    
    souceFile =sys.argv[1]
    destinationFile =sys.argv[2]

    fobj1 = open(souceFile,"r")
    data =fobj1.read()

    fobj2 = open(destinationFile,"w")
    fobj2.write(data)

    fobj1.close()
    fobj2.close()

    print("content copied sucessfully ")

    
if __name__ == "__main__":
    main()