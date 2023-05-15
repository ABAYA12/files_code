def main():
    numeric = open("calculation.txt", "w")
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    num3 = int(input("Enter a third number: "))

    numeric.write(str(num1) + "\n")
    numeric.write(str(num2) + "\n")
    numeric.write(str(num3) + "\n")

    numeric.close()


main()


def read():
    data = open("calculation.txt", "r")
    num1 = int(data.readline())
    num2 = int(data.readline())
    num3 = int(data.readline())

    data.close()

    total = num1 + num2 + num3
    print(f"The numbers are {num1}, {num2}, {num3}.")
    print(f"The sum total of the three numbers is {total:.2f}")


read()
