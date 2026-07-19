import threading
def evenFactors(no):
    Sum = 0
    for i in range(1,no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i,end =" ")
            Sum = Sum + i
    print("\nsummation of Even factors are :-",Sum)




def OddFactors(no):
    Sum = 0
    for i in range(1,no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i,end = " ")
            Sum = Sum + i
    print("\nsummation of odd factors are :-",Sum)

def main():
    num = int(input("enter the number :- "))
    tobj1 = threading.Thread(target =evenFactors,args=(num,))
    tobj2 = threading.Thread(target = OddFactors,args=(num,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")
if __name__ == "__main__":
    main()
