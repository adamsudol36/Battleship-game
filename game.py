from matrix_generation import (
    show_actual_board,
    make_player_matrix,
    generate_computer_matrix,
    get_basic_info
)
from game_functions import (
    show_actual_state,
    better_bot_shoot,
    player_shoot
)
from time import sleep


def main():
    '''
    Whole game function.
    Gets info from player. Creates bot and player fleets.
    Conducts whole game process and when needed, prints
    messages to player.
    '''
    introduction()
    dim, size_list = get_basic_info()
    Bot_Matrix, Bot_Fleet = generate_computer_matrix(size_list, dim)
    Player_Matrix, Player_Fleet = make_player_matrix(size_list, dim)
    print('Grajmy!')
    show_actual_state(Player_Matrix, Bot_Matrix, dim)
    shot_list = []
    while Player_Fleet.if_fleet_is() and Bot_Fleet.if_fleet_is():
        result_b, result_p = True, True
        while result_p:
            Bot_Matrix, Bot_Fleet, result_p = player_shoot(Bot_Matrix,
                                                           Bot_Fleet, dim)
            if not Bot_Fleet.if_fleet_is():
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
                print('Wygrałeś!')
                print('Koniec gry :)')
                return
            else:
                print(show_actual_board(Bot_Matrix.get_matrix(), dim, True))
                print('Gramy dalej')
        else:
            show_actual_state(Player_Matrix, Bot_Matrix, dim)
        while result_b:
            (Player_Matrix, result_b,
             Player_Fleet, shot_list) = better_bot_shoot(Player_Matrix,
                                                         Player_Fleet,
                                                         shot_list, dim)
            if not Player_Fleet.if_fleet_is():
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
                print('Przegrałeś!')
                print('Koniec gry :)')
                return
            else:
                show_actual_state(Player_Matrix, Bot_Matrix, dim)
        else:
            show_actual_board(Player_Matrix.get_matrix(), dim)
            print('Gramy dalej')


def introduction():
    '''
    Makes introduction in polish
    '''
    print('Dzień dobry!')
    print('Zaczynasz grę w statki.')
    print('Na początek kilka reguł.')
    print('Statki nie mogą leżeć obok siebie ani się przecinać.')
    print('Czytaj, nie mogą się nakładać ani stykać rogami czy bokami.')
    print('Czytaj uważnie co gra do Ciebie pisze.')
    print('Ilość statków i wielkość planszy będzie zależała od Twojego wyboru')
    print('Będziesz miał do dyspozycji statek o największej ilości kadłubów')
    print('o jeden mniej statków o ilości kadłubów mniejszej o jeden etc.')
    print('Jeżeli generowanie planszy będzie trwało zbyt długo,')
    print('zresetuj grę.')
    print('W odpowiednich momentach będzie wyświetlana Twoja plansza')
    print('bądź plansza przeciwnika albo obie:')
    print('Twoja po lewej, bota po prawej stronie.')
    print('A oto oznaczenia:')
    print('□  - to oznacza, że w tym miejscu jest Twój statek')
    print('⊠  - to oznacza, że statek został trafiony.')
    print('○   - to oznacza, że w tym miejscu zostało spudłowane')
    print('Miłej gry życzę :)')
    sleep(20.)


if __name__ == '__main__':
    main()
