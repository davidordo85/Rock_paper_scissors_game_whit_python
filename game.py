

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
    pass

def is_exit(user_choice):
    '''
    Predicado qeu devuelve True si el usuario ha decidido parar y False
    si quiere seguir jugando
    '''
    return True

def generate_computer_choice():
    '''
    Genera y devuelve una jugada al azar
    '''
    pass

def evaluate_move(user_choice, comp_choice):
    ''' 
    Compara las dos jugadas y devuelve un texto con el resultado
    '''
    pass

def print_result(user_choice):
    '''
    Imprime en bonito el resultado
    '''
    pass

if __name__ == "__main__":
    print("ma llamao alguien?")
    game_loop()