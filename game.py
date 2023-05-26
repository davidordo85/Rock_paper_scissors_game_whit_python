import random

def game_loop():
    '''
    Start the main game loop
    '''
    while True:
        user_choice = read_user_choice()
        if not is_exit(user_choice):
            comp_choice = generate_computer_choice()
            result = evaluate_move(user_choice, comp_choice)
            print_result(result)
        else:
            break

def read_user_choice():
    '''
    Read a user selection (rock, paper, scissors, or exit)
    '''
    print("Select an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    user_choice = ''
    option = input("Enter the number of the desired option: ")

    if option == '1':
        user_choice = 'Rock'
        print("you have chosen: " + user_choice)
    elif option == '2':
        user_choice = 'Paper'
        print("you have chosen: " + user_choice)
    elif option == '3':
        user_choice = 'Scissors'
        print("you have chosen: " + user_choice)
    elif option == '4':
        user_choice = 'exit'
    else:
        print("Invalid option")
    
    return user_choice

def is_exit(user_choice):
    '''
    Predicate that returns True if the user has decided to stop and False
    if you want to continue playing
    '''
    is_exit = False
    if user_choice == 'exit':
        is_exit = True
    return is_exit

def generate_computer_choice():
    '''
    Generate and return a random play
    '''
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    return comp_choice


def evaluate_move(user_choice, comp_choice):
    ''' 
    Compares the two plays and returns a text with the result
    '''
    if user_choice == comp_choice:
        result = user_choice + ' Deuce ' + comp_choice
    elif ((user_choice == 'Rock' and comp_choice == 'Scissors')
     or (user_choice == 'Paper' and comp_choice == 'Rock')
     or (user_choice == 'Scissors' and comp_choice == 'Paper')):
        result = user_choice + ' wins ' + comp_choice
    else:
        result = user_choice + ' loses ' + comp_choice
    return result

def print_result(result):
    '''
    Print the result
    '''
    print('You ' + result + ' Computer')

if __name__ == "__main__":
    game_loop()