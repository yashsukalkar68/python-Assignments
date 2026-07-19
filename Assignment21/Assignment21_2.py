import threading
def maximum(data):
    Max = data[0]
    for i in data:
        if i > Max:
            Max = i
    print("Max :-",Max)
def Minimum(data):
    Min = data[0]
    for i in data:
        if i < Min:
            Min = i
    print("Min :-",Min)

    
def main():
    

    data = []
    
    size = int(input("enter the numbers:-"))
    for i in range(size):
        value = int(input())
        data.append(value)

    t1 = threading.Thread(target =maximum,args =(data,))
    t2 = threading.Thread(target = Minimum,args =(data,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

   
   

if __name__ =="__main__":
    main()