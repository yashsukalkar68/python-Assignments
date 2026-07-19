from multiprocessing import Pool
def Prime(no):   
    if no <= 0:
        return False
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

def main():
    data = [100000,20000,30000,40000]
    with Pool(4) as p:
        mdata = p.map(Prime,data)

    print(mdata)

if __name__ == "__main__":
    main()

