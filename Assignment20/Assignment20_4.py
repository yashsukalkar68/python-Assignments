import threading
def Small(Str):
    print("Thread ID   :", threading.get_ident())
    print("Thread ID   :", threading.get_ident())
    print("Small letters:")
    for i in Str:
        if i >= 'a' and i <= 'z':
            print(i)

def Captil(Str):
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())
    print("Capital letters:")
    for i in Str:
        if i >= 'A' and i<= 'Z':
            print(i)

def Digit(Str):
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())
    print("Digits in letters:")

    for i in Str:
        if i >= '0' and i <= '9':
            print(i)

def main():
    data = input("enter a string : ")

    t1=threading.Thread(target = Small,args=(data,) )
    t2=threading.Thread(target = Captil,args=(data,))  
    t3=threading.Thread(target = Digit,args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ =="__main__":
    main()