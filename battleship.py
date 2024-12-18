import random
import os
from player import Player
from ship import Ship
from board import Board

available_ships = [
    {"name": "Battleship", "length": 5},
    {"name": "Cruiser", "length": 4},
    {"name": "Destroyer", "length": 3},
    {"name": "Sub", "length": 2}
]

difficulties = {
    "easy" : [5, 5, 1],
    "medium" : [8, 8, 2],
    "hard" : [10, 10, 4]
}

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')

    else:
        os.system('cls')
    print("Witaj w grze w statki\n")

def get_shot(player, rows, columns):
    shot = []
    target = input("\nWprowadź cel w formacie WIERSZ, KOLUMNA Dla przykładu:\n\nA,1\n\nCel: ")
    try:
        target = target.split(",")
        for coordinate in target:
            try:

                shot.append(int(coordinate)-1)
            except:

                shot.append(ord(coordinate)-65)


        if shot[0] >= rows or shot[1] >= columns:
            print("Musisz wprowadzić współrzędne, które znajdują się na planszy. Spróbuj ponownie.")
            return False

        if shot in player.shots_fired:
            print("Już próbowałeś tych współrzędnych. Spróbuj ponownie!")
            return False

        else:
            player.shots_fired.append(shot)
            return shot
    except:
        print("Proszę podać prawidłową współrzędną.")
        return False

def get_players():
    players = []
    while True:
        num_players = input("Możesz grać w grę w statki jako gracz 1 lub 2.\n\n1. 1 gracz\n2. 2 graczy\n\n")
        if num_players == "1":
            clear_screen()
            name = input("\nJak masz na imię?\n\n")
            players.append(Player(name))
            break
        elif num_players == "2":
            clear_screen()
            name = input("\nJakie jest imię gracza 1?\n\n")
            players.append(Player(name))
            clear_screen()
            name = input("\nJakie jest imię gracza 2?\n\n")
            players.append(Player(name))
            break
        else:
            clear_screen()
            print("Proszę wprowadzić prawidłową opcję, 1 lub 2")
    return players


def get_difficulty():
    difficulty = int(input("""Wybierz poziom trudności:\n\n
        1. Łatwy
        2. Średni
        3. Trudny\n\n"""))
    clear_screen()
    return difficulty

def one_player_game():
    clear_screen()
    turn = 0
    while players[0].ships_remaining > 0:

        print("\nPlansza {player}".format(player = "Komputera"))
        print(players[0].board.print_board(False))

        while True:
            shot = get_shot(players[0],players[0].board.rows, players[0].board.columns)
            if shot != False:
                break
        clear_screen()
        print("\nPlansza {player}\n".format(player = "Komputera"))
        hit = players[0].board.update_board(shot)
        if hit == "hit":
            for ship in players[0].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk == True:
                        players[0].ships_remaining -= 1
        turn += 1
        clear_screen()
    finish = input("Koniec gry! Zajęło Ci to {turns} tur, aby wygrać. Naciśnij Enter, aby zakończyć grę".format(turns = turn))
    clear_screen()

def two_player_game():
    clear_screen()
    turn = 0
    attacker = 0
    defender = 0
    while players[defender].ships_remaining > 0:
        attacker = turn % 2
        if attacker == 0:
            defender = 1
        else:
            defender = 0

        print("Tura gracza {player}".format(player = players[attacker].name))
        print("\nPlansza {player}".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\nPlansza {player}".format(player = players[defender].name))
        print(players[defender].board.print_board(False))

        while True:
            shot = get_shot(players[attacker],players[defender].board.rows, players[defender].board.columns)
            if shot != False:
                break
        clear_screen()
        print("Tura gracza {player}".format(player = players[attacker].name))
        print("\nPlansza {player}".format(player = players[attacker].name))
        print(players[attacker].board.print_board(True))

        print("\nPlansza {player}\n".format(player = players[defender].name))
        hit = players[defender].board.update_board(shot)
        if hit == "hit":
            for ship in players[defender].ships:
                if shot in ship.coordinates:
                    ship.hit()
                    if ship.sunk == True:
                        players[defender].ships_remaining -= 1
        input("\nNaciśnij Enter, aby przekazać komputer swojemu partnerowi")
        clear_screen()
        input("Naciśnij Enter, kiedy będziesz gotowy")
        clear_screen()
        turn += 1
    finish = input("Koniec gry! Naciśnij Enter, aby zakończyć grę")
    clear_screen()


clear_screen()
players = get_players()


while True:
    difficulty = get_difficulty()
    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        break
    print("Nieprawidłowy wybór\n")


for player in players:
    if difficulty == 1:
        player.get_board(difficulties["easy"][0:2])
        player.get_ships(difficulties["easy"][2], available_ships)
    elif difficulty == 2:
        player.get_board(difficulties["medium"][0:2])
        player.get_ships(difficulties["medium"][2], available_ships)
    elif difficulty == 3:
        player.get_board(difficulties["hard"][0:2])
        player.get_ships(difficulties["hard"][2], available_ships)

for player in players:
    player.place_ships()


if len(players) == 1:
    one_player_game()
else:
    two_player_game()