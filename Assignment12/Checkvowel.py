def CheckVowel(a):
    vowels =["a","e","i","o","u"]

    if a in vowels:
        return True
    else :
        return False
    

def main():

    print("enter the Alaphabet :")
    char = input()

    ret = CheckVowel(char)

    if ret:
        print("vowel")
    else:
        print("conconent") 

if __name__ =="__main__":
    main()
