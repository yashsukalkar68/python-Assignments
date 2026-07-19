import os 
def main():
    Files = input("enter the file name :-")
    found = False
    for FolderName , SubFolder, FileName in os.walk("."):
        if Files in FileName:
            print("file is presnet :",Files)
            found = True
            break
    if not found:
        print("file is not present :",Files)

if __name__ == "__main__":
    main()