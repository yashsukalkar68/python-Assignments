def DiplayGrades(no):
    if no >= 75:
        return "Distinction"
    elif no>=60:
        return "first class"
    elif no >=50:
        return "secound class"
    else:
        return "Fail"
def main():

    Marks = int(input("enter marks :"))

    Grade = DiplayGrades(Marks)

    print("Grades :",Grade)
  


if __name__ == "__main__":
    main()