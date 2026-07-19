from multiprocessing import Pool
import os
def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    print("Process Id",os.getpid())
    return fact

def main():
    data = [10,15,20,25]
    with Pool(4) as p:
        mdata = p.map(Factorial,data)

    print("input is ",data)
    print("factorial",mdata)

if __name__ == "__main__":
    main()

