def main():
    # ask user for the number of sales
    days = int(input("how many time did sale this week: "))

    for count in range(1, days + 1):
        # Ask user to enter sale amount
        selling = float(input('Enter sales amount: '))

        # open the file to wrote to
        sale = open("selling.txt", "w")
        sale.write(str(selling) + "\n")

        # close the file
        sale.close()


main()
