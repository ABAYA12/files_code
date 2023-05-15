def main():
    # creat a bool variable to use as a flag
    found = False

    # Get the search value from the user
    search = input('Enter a description to search for: ').rstrip().lstrip()

    # open the file
    read_coffee = open("coffee.txt", "r")
    # read the first line of the coffee file
    description = read_coffee.readline()
    while description != '':
        # read the next line
        quantity = float(read_coffee.readline())
        description = description.rstrip('\n')

        # Check whether the search value match description
        if description == search.lower():
            print(f"Description: {description.title()}")
            print(f"Quatity: {quantity}")
            print()

            # set the found flag to true
            found = True
        description = read_coffee.readline()
    # close the file
    read_coffee.close()

    # If the search value was not found in the file, display a message
    if not found:
        print("Description cannot be found. Make sure you entered the correct name")


if __name__ == '__main__':
    main()
