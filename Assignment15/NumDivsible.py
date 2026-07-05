Divisible = lambda no: no % 3 == 0 and no % 5 == 0
def main():

    data = [2,13,23,45,4,56,10,12,9,15]


    Fdata = list(filter(Divisible,data))

    print("number divisible by 3 and 5 are :",Fdata)

if __name__ == "__main__":
    main()