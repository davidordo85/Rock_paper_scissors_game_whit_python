import random

def game_loop():
    '''
    Arranca el bucle principal del juego
    '''
    while True:
        # Leo la selección del usuario (piedra, papel, tijera o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: salgo
            break

def read_user_choice():
    '''
    Lee una selección del usuario (piedra, papel, tijera o salir)
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
    Predicado qeu devuelve True si el usuario ha decidido parar y False
    si quiere seguir jugando
    '''
    is_exit = False
    if user_choice == 'exit':
        is_exit = True
    return is_exit

def generate_computer_choice():
    '''
    Genera y devuelve una jugada al azar
    '''
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    return comp_choice


def evaluate_move(user_choice, comp_choice):
    ''' 
    Compara las dos jugadas y devuelve un texto con el resultado
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
    Imprime en bonito el resultado
    '''
    print('You ' + result + ' Computer')

if __name__ == "__main__":
    game_loop()