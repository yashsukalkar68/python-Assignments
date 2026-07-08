def PrintEven():
    data = []
    for i in range(1,11):
        data.append(i*2)
    return data

def main():
    ret = PrintEven()
    for i in ret:
        print(i)

if __name__ == "__main__":
    main()
