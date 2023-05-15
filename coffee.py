def main():
    # set a control variable for the while loop
    again = "y"
    while again == "y":
        # display the name of the company
        print("ROSTER INC.")

        # open the coffee file
        coffe_file = open("coffee.txt", "a")

        # collect description and quantity from user
        description = input("Enter description of coffee: ")
        quantity = int(input("Enter quantity of coffee: "))

        # write to the coffee file
        coffe_file.write(f"{description}\n")
        coffe_file.write(str(quantity) + "\n")

        # ask if user wants to enter another coffee details
        print("Do you want to enter another details?")
        again = input("Enter 'y' for yes and 'n' for no(y/n): ")

    # close the file
    coffe_file.close()


main()


# Read from the infile above
def read_file():
    read_coffee = open("coffee.txt", "r")
    # read the first line of the coffee file
    description = read_coffee.readline()
    while description != '':
        # read the next line
        quantity = float(read_coffee.readline())
        description = description.rstrip('\n')

        print(f"Description: {description.title()}")
        print(f"Quatity: {quantity}")
        # raed the file again
        description = read_coffee.readline()
    # close the file
    read_coffee.close()


read_file()
