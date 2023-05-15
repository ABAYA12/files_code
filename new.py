def main():
    register = open("names.txt", "w")
    register.write("Alex\n")
    register.write("Abaya\n")
    register.write("Benjy\n")
    register.write("Brian\n")
    register.write("Jeff\n")
    register.close()


main()


def read():
    call_reg = open("names.txt", "r")
    response = call_reg.read()
    call_reg.close()
    print(response)


read()
