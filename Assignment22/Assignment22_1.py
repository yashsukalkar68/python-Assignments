from multiprocessing import Pool

def SumSquare(no):
    total = 0
    for i in range(1,no+1):
        total += i*i
    return total

def main():
    data = [100000,200000,300000,400000]
    with Pool(4) as p:
        mdata = p.map(SumSquare,data)
    print(mdata)

if __name__ == "__main__":
    main()

