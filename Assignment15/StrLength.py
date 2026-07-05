LengthCount = lambda  str : len(str) >=5
def main():

    Str =["python","c","java","program"]

    Fdata =list(filter(LengthCount,Str))

    print("string having length greater than 5",Fdata)


if __name__ == "__main__":
    main()