import Arithmetic

def Operations(no1,no2):
    Ans1 = Arithmetic.Add(no1,no2)
    Ans2 =  Arithmetic.Sub(no1,no2)
    Ans3 =  Arithmetic.Mult(no1,no2)
    Ans4 =  Arithmetic.Div(no1,no2)
    
    return Ans1,Ans2,Ans3,Ans4
def main():

    a = int(input("enter first  the number :- "))
    b = int(input("enter secound the number :- "))
    
    ret1,ret2,ret3,ret4 = Operations(a,b)
    print(f"Add:- {ret1}")
    print (f"Sub:- {ret2}")
    print(f"Mult:- {ret3}")
    print(f"Div:- {ret4}")

if __name__ == "__main__":
    main()