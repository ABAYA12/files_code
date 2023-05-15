# define a "main()" function to handle the piece of program
def main():
    # Open 'a sales_file' as file object and name it 'sales' as file name
    sales_file = open("sales.txt", "w")  # The mode is write-mode('w')
    # Now, collect the sales amount from the user for 3 times
    sale1 = int(input("Enter your first sales: "))
    sale2 = int(input("Enter your second sales: "))
    sale3 = int(input("Enter your third sales: "))
    # write or save the sales amount collected from the user to sales_file and convert it to a string('str')
    sales_file.write(str(sale1) + "\n")
    sales_file.write(str(sale2) + "\n")
    sales_file.write(str(sale3) + "\n")
    # close the file
    sales_file.close()


# call the main() function
main()


# read from the file above
def read():
    # open the file
    infile = open("sales.txt", "r")
    # read each line of the file and convert it to an integer using 'int'
    sale1 = int(infile.readline())
    sale2 = int(infile.readline())
    sale3 = int(infile.readline())

    # calculating the total sales
    total = sale1 + sale2 + sale3
    # display the output
    print(f"Your sales are {sale1},{sale2},{sale3}")
    print(f"Total Sales: ${total:.2f}")

    # close infile
    infile.close()


# call read() function
read()
