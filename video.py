# define a main() function
def main():
    # Get the number of videos from the user
    num_videos = int(input("How many videos have you recorded?: "))
    # open a file to write to
    videos = open("video.txt", "w")
    for count in range(1, num_videos + 1):
        # Get the duration in seconds of videos recorded by the user
        video = float(
            input(f"Enter the duration seconds for each video. #Video {count}: "))
        # Write the duration to the file object(videos)
        videos.write(f"{video}\n")
        # display an out to tell the user where the duration has been saved to
    print("You data has been saved to video.txt")
    # Close the videos file
    videos.close()


main()


def read():
    # set an accummulator
    total = 0

    # initialize a variable to keep count of the videos
    count = 0
    open_video = open("video.txt", "r")
    for line in open_video:
        run_time = float(line)

        count += 1
        print(f"#Video {count}: {run_time}", sep="")

        total += run_time
    open_video.close()
    print(f"Your total duration is {total:.2f} seconds")


read()
