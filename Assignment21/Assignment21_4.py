import threading
def Thread1(data):
    Total = 0
    for no in data:
        for i in range(1,no+1):
            Total += i
    print("sum :-",Total)

def Thread2(data):
    product = 1
    for i in data:
        product *= i

    print("product :-",product)
def main():

    data = [1,3,5,3,45]

    t1 = threading.Thread(target =Thread1,args =(data,))
    t2 = threading.Thread(target = Thread2,args =(data,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ =="__main__":
    main()