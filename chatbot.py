import random

exercises = []
session_history = []

def main():
    # Opening the txt file and splitting the contents into a list
    with open("home_workouts.txt", 'r') as file_data:
        for line in file_data:
            data = line.split()
            exercises.append(data)
    
    print("I am a fitness chatbot that suggests different types of workouts. Each workout is designed to be done at home!")

    while True:
        user_input = input("What type of body part would you like to work out? Legs, back, chest, biceps, triceps, core? Type 'history' to see session history. Type 'quit' to exit: ").lower().strip()

        if user_input == "history":
            print_session_history()

        if user_input == "legs":
            store_history(user_input)
            print(get_legs())
        
        elif user_input == "back":
            store_history(user_input)
            print(get_back())
        
        elif user_input == "chest":
            store_history(user_input)
            print(get_chest())
        
        elif user_input == "biceps":
            store_history(user_input)
            print(get_biceps())
        
        elif user_input == "core":
            store_history(user_input)
            print(get_core())
        
        elif user_input == "quit":
            print("Goodbye")
            break
        
        else:
            print("Invalid input. Try again")


def get_legs():
    legs = exercises[0]
    return random.choice(legs)


def get_back():
    back = exercises[1]
    return random.choice(back)


def get_chest():
    chest = exercises[2]
    return random.choice(chest)


def get_biceps():
    biceps = exercises[3]
    return random.choice(biceps)


def get_triceps():
    triceps = exercises[4]
    return random.choice(triceps)


def get_core():
    core = exercises[5]
    return random.choice(core)


def store_history(user_input):
    session_history.append(user_input)


def print_session_history():
    if not session_history:
        print("No session history.")
        return
    
    print("Session history: ")
    for entry in session_history:
        print(entry)


if __name__ == "__main__":
    main()
