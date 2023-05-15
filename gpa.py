def main():
    GPA = open("grades.txt", "w")
    print("You are suppose to enter your grades one by one for your CGPA calculation")
    grade1 = int(input("Enter a grade here, eg. 12 for 'A' (80 and above ): "))
    grade2 = int(input("Enter another grade here:"))
    grade3 = int(input("Enter another grade here:"))
    grade4 = int(input("Enter another grade here:"))
    grade5 = int(input("Enter another grade here:"))
    grade6 = int(input("Enter another grade if any. else enter 0: "))

    GPA.write(str(grade1) + "\n")
    GPA.write(str(grade2) + "\n")
    GPA.write(str(grade3) + "\n")
    GPA.write(str(grade4) + "\n")
    GPA.write(str(grade5) + "\n")
    GPA.write(str(grade6) + "\n")

    GPA.close()


main()


def read():
    gpa = open("grades.txt", "r")
    grade1 = int(gpa.readline())
    grade2 = int(gpa.readline())
    grade3 = int(gpa.readline())
    grade4 = int(gpa.readline())
    grade5 = int(gpa.readline())
    grade6 = int(gpa.readline())

    print(
        f"Your grades are {grade1},{grade2},{grade3},{grade4},{grade5},{grade6}")
    if grade6 == 0:
        CGPA = (grade1 + grade2 + grade3 + grade4 + grade5) / 15
        print(f"Your CGPA = {CGPA:.2f}")
    elif grade6 > 0:
        CGPA = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6) / 16
        print(f"Your CGPA = {CGPA:.2f}")
    append = open("grades.txt", "a")
    append.write("CGPA: ")
    append.write(str(CGPA) + "\n")

    gpa.close()


read()
