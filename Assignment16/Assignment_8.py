def CehckNum():
    data =[]
    for i in range(5):
        data.append("*")
    return data
def main():
    
    ret = CehckNum()
    for i in ret:
        print(i)
if __name__ == "__main__":
    main()
