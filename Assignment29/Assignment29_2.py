
def main():
    try:
        Files = input("enter the file name :-")

        fobj = open(Files, "r")
        data = fobj.read()

        print(data)

        fobj.close()
        
    except FileNotFoundError:
        print("File is not present in current directory..! ")
if __name__ == "__main__":
    main()