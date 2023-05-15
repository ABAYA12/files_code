def main():
    # Ask user for the nummber of subjects
    num_subjects = int(input("How many subjects did you study this term?: "))
    # open a file and name it
    subject_file = open("score.txt", "w")
    # use the for loops to iterate and ask for scores the number of subjects the user entered
    for count in range(1, num_subjects + 1):
        # Take the scores of subjects from the user and convert it to float
        subjects = float(
            input(f"Enter your scores one by one. #subject {count}: "))

        subject_file.write(f"{subjects}\n")

    subject_file.close()
    # Display the statement below to tell the user where the file has been saved to
    print("Scores have been saved to score.txt file")


# Call the main function for the program to execute and stop but without an output
main()


# READING FROM THE FILE(NUMS_SUBJECTS) ABOVE
def read():
    total = 0  # an accummulator
    count = 0  # a count variable for displaying each subject
    sub = 0  # a count variabble for adding number of each subjects total score which is 100
    add_subjects = open("score.txt", "r")
    name = str(input("Enter your full name (first name first): "))
    subject_file = open("score.txt", "a")
    subject_file.write(name.title() + "\n")
    subject_file.write("-----------------------------------\n")
    subject_file.close()

    status1 = "PROMOTED"
    status2 = "REPEATED"

    for line in add_subjects:
        add_score = float(line)
        count += 1
        print(f"Subject #{count}: {add_score:.2f}", sep="")
        # add to score of each subject to the total
        total += add_score
        average = total / count
        # Adding the total mark of all subjects by default which is 100
        sub += 100
    # Close the file
    add_subjects.close()
    # Display the results
    print(f"TOTAL SCORE: {total:.2f} / {sub}")
    print(f"AVERAGE SCORE: {average:.2f}")

    # Append the total and average marks to score.txt
    subject_file = open("score.txt", "a")
    subject_file.write(f"Total: {total} / {sub}\n")
    subject_file.write(f"Average Score: {average}\n")

    pass_mark = 75  # set a pass mark for the if-elif-esle statement
    # Compare average mark to pass mark and display an output
    if average < pass_mark:
        print(
            f"Your average score is {average:.2f}. You are not qualified for the certification and promotion.")
        print(f"Status: {status2}")
        subject_file = open("score.txt", "a")
        subject_file.write(f"Status: {status2}\n")

    elif average >= pass_mark:
        print(
            f"Congratulations,your average score is {average:.2f}. You have been promoted to the next class.")
        print(f"Status: {status1}")
        subject_file = open("score.txt", "a")
        subject_file.write(f"Status: {status1}\n")


# Call the read function for the program to execute and diplay an output
read()
