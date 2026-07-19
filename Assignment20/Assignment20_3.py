import threading
def evenFactors(data):
    even =[]
    Sum = 0
    for i in data:
        if i % 2 == 0:
            even.append(i)
            Sum = Sum + 1
    print("summation of Even number are :-",Sum)
    print("even numbers are ",even)



def OddFactors(data):
    odd =[]
    Sum = 0
    for i in data:
        if  i % 2 != 0:
            odd.append(i)
            Sum = Sum + 1
    print("summation of odd  are :-",Sum)
    print("odd numbers are :-",odd)
def main():
    num = [10,22,12,23,34,32,311,21,23,67,54,7,7,865,21]
    tobj1 = threading.Thread(target =evenFactors,args=(num,))
    tobj2 = threading.Thread(target = OddFactors,args=(num,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Exit from main")
if __name__ == "__main__":
    main()
