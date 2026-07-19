import threading
def Prime(data):
    prime=[]
    for no in data:
        count = 0

        for i in range(1,no+1):
            if no % i == 0:
                count +=1
        
        if count ==2:
            prime.append(no)
    print("prime ;-",prime)

def NonPrime(data):
    NonPrime=[]
    for no in data:
        count = 0
        for i in range(1,no+1):
            if no % i == 0:
                count +=1

        if count !=2:
            NonPrime.append(no)
    print("non Prime :-",NonPrime)

def main():
    data = [10,2,4,23,56,57,68,87,7,5,42,35,33,13,24,34,7,]


    t1 = threading.Thread(target = Prime,args =(data,))
    t2 = threading.Thread(target = NonPrime,args =(data,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

   
   

if __name__ =="__main__":
    main()