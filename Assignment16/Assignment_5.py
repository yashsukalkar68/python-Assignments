def Display():
    data= []
    for i in range(9,0,-1):
        data.append(i)
    return data

def main():
    ret = Display()
    print(ret)

if __name__ == "__main__":
    main()
