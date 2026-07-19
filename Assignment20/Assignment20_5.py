import threading
def Thread1():
    for i in range(1,51,1):
        print(i)
def Thread2():
    print("reverse Order :")
    for i in range(50,-1,-1):
        print(i)
        
def main():
    
    t1=threading.Thread(target = Thread1,args=())
    t2=threading.Thread(target =Thread2,args=())  


    t1.start()
    t1.join()

    t2.start()
    t2.join()

  

if __name__ =="__main__":
    main()