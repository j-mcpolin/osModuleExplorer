import os

def create_directories():
    """Create a series of nested directories with clues."""
    # Define the base directory
    base_directory = "TaskDirectory"

    # Create the main directory
    os.makedirs(base_directory, exist_ok=True)

    # Level 1 Directory Structure
    level1_path = os.path.join(base_directory, "Level1")
    os.makedirs(level1_path, exist_ok=True)

    # Create subdirectories for Level 1
    os.makedirs(os.path.join(level1_path, "RoomA"), exist_ok=True)
    os.makedirs(os.path.join(level1_path, "RoomB"), exist_ok=True)
    os.makedirs(os.path.join(level1_path, "RoomC"), exist_ok=True)

    # Create a final clue file in Room A
    with open(os.path.join(level1_path, "RoomA", "final_clue.txt"), "w") as file:
        file.write("You made it through Level 1!")

    # Level 2 Directory Structure
    level2_path = os.path.join(base_directory, "Level2")
    os.makedirs(level2_path, exist_ok=True)

    # Create subdirectories for Level 2
    os.makedirs(os.path.join(level2_path, "SecretRoom"), exist_ok=True)
    os.makedirs(os.path.join(level2_path, "HiddenChamber"), exist_ok=True)

    # Create a final clue file in in the Hidden Chamber
    with open(os.path.join(level2_path, "HiddenChamber", "final_clue.txt"), "w") as file:
        file.write("You made it through Level2!")

    secretRoom_path = os.path.join(level2_path, "SecretRoom")
    os.makedirs(os.path.join(secretRoom_path, "InTheAttic"), exist_ok=True)


    print("Directory structure created successfully.")

if __name__ == "__main__":
    create_directories()
