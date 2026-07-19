import threading

def SumEven():

    for i in range(2,21,2):
        print(i)

def SumOdd():

    for i in range(1,20,2):
        print(i)


def main():
    
    
    tobj1 = threading.Thread(target=SumEven, name="Even")
    tobj2= threading.Thread(target=SumOdd, name="Odd")

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
    

 
if __name__ == "__main__":
    main()
