import os
from pathlib import Path

BASEDIRECTORY = os.getcwd() #constant to keep track of your start point

def LevelOne():
    startingDir = "TaskDirectory/Level1"
    try:
        # Change to Level 1 directory
        os.chdir(startingDir)

        print("Current directory:" + os.getcwd())
        print("Welcome to Level 1! Use 'os.listdir()' to see available folders.")
        print("Contents of Level 1:")

        #  Use 'os.listdir()' to see available folders.
        # TODO

        # Change to Room A using os.chdir()
        # TODO

        # use os.chdir to change to the Room A
        # TODO

        # print your current directory
        # TODO

        # print the directories in Room A
        # TODO

        # when you find the final clue, open it, and read and print the message
        # TODO

    except Exception as e:
        print("Error navigating to Level 1:" + e)

def Level2():

    try:
        # Change to Level 2 directory
        os.chdir(BASEDIRECTORY + "/TaskDirectory/Level2/SecretRoom/InTheAttic")

        # print your current working directory
        # TODO
        # print the contents of the directory
        # TODO

        # this should be a dead end!

        # Go back to parent directory
        # first, I will get the current working directory for you
        path = os.getcwd()
        # print current directory
        # TODO


        # use the following code to find the parent directory
        # what do you think should be where the ? is
        # TODO
        # parent = Path(os.path.dirname(path)).resolve().parents[?]

        # print all directories
        # TODO

        # go to the hidden chamber
        #TODO

        # Change to the Hidden Chamber
        # TODO


        # Read and print the final clue
        # TODO


    except Exception as e:
        print("Error navigating to Level 2:" + e)

def main():
    """Main function to guide students through navigation tasks."""
    print("Welcome to the Directory Navigation Task!")

    # Task 1: Navigate to Level 1
    print("\nNavigating to Level 1...")
    LevelOne()

    # Task 2: Navigate to Level 2
    print("\nNavigating to Level 2...")
    Level2()

main()

