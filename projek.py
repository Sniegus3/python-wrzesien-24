import random
 
punkty = {}
 
def menu():
    print()
    print("---------------------")
    print("      MENU GRY        ")
    print("---------------------")
    print("1. Nowa gra")
    print("2. Pokaz wyniki")
    print("3. Wyjście")
    while True:
        try:
            wybor = int(input("Twój wybór (1, 2, 3): "))
            if wybor == 1:
                return 'nowa_gra'
            elif wybor == 2:
                show_scores()
                continue
            elif wybor == 3:
                print("Dziękujemy za grę!")
                return 'koniec'
            else:
                print("Wybierz poprawną opcję: 1, 2 lub 3.")
        except ValueError:
            print("Wprowadź liczbę 1, 2 lub 3.")
 
 
def name_of_player():
    while True:
        name_of_player = input("Wprowadź nazwę gracza: ")
        if name_of_player:
            return name_of_player
 
 
def choose_range():
    while True:
        try:
            print("Podaj zakres zgadywanej liczby.")
            dolny = int(input("Podaj dolny zakres: "))
            gorny = int(input("Podaj górny zakres: "))
            if dolny >= gorny:
                print("Dolny zakres musi być mniejszy od górnego. Spróbuj ponownie.")
            else:
                return gorny, dolny
        except ValueError:
            print("Wprowadź liczby całkowite.")
 
 
def difficulty_level():
    print()
    print("Wybierz poziom trudności: ")
    print("1. Łatwy (nielimitowana liczba prób)")
    print("2. Średni (10 prób)")
    print("3. Trudny (5 prób)")
    while True:
        try:
            wybor = int(input("Twój wybór (1, 2, 3): "))
            if wybor == 1:
                return None
            elif wybor == 2:
                return 10
            elif wybor == 3:
                return 5
            else:
                print("Wybierz poprawną opcję: 1, 2 lub 3.")
        except ValueError:
            print("Wprowadź liczbę 1, 2 lub 3.")
 
 
def gra(dolny, gorny, max_prob, poziom, gracz):
    liczba_do_zgadniecia = random.randint(dolny, gorny)
    liczba_prob = 0
    print(f"\nKomputer wylosował liczbę z zakresu {dolny} - {gorny}. Spróbuj ją zgadnąć.")
 
    while True:
        try:
            strzal = int(input("Podaj swoją liczbę: "))
            liczba_prob += 1
            if strzal < liczba_do_zgadniecia:
                print("Za mało!")
            elif strzal > liczba_do_zgadniecia:
                print("Za dużo!")
            else:
                print(f"Trafiłeś! Liczba to {liczba_do_zgadniecia}.")
                print(f"Udało ci się w {liczba_prob} próbach.")
                punkt = oblicz_punkty(poziom, max_prob, liczba_prob)
                if gracz not in punkty:
                    punkty[gracz] = 0
                punkty[gracz] += punkt
                print(f"Zdobyłeś {punkt} punktów. Łącznie masz {punkty[gracz]} punktów.")
                return True
            if max_prob is not None and liczba_prob >= max_prob:
                print(f"Przegrałeś! Wykorzystałeś wszystkie {max_prob} próby. Prawidłowa liczba to {liczba_do_zgadniecia}.")
                return False
        except ValueError:
            print("Wprowadź poprawną liczbę.")
 
 
def oblicz_punkty(poziom, max_prob, liczba_prob):
    if poziom == "łatwy":
        return 10  
    elif poziom == "średni":
        return max(0, 100 - (liczba_prob * 10))  
    elif poziom == "trudny":
        return max(0, 200 - (liczba_prob * 40))  
 
 
def show_scores():
    print("\n---------- Wyniki graczy ----------")
    if not punkty:
        print("Brak zarejestrowanych wyników.")
    else:
 
        print(f"{'Gracz':<20} {'Punkty'}")
        print("-" * 30) 
 
 
        for gracz, wynik in punkty.items():
            print(f"{gracz:<20} {wynik}")
 
    print("------------------------------------")
 
 
def play_again():
    while True:
        wybor = input("Czy chcesz zagrać ponownie? (tak/nie): ").strip().lower()
        if wybor == "tak":
            return True
        elif wybor == "nie":
            print("Dziękujemy za grę! Oto wyniki:")
            show_scores()  
            return False
        else:
            print("Wybierz 'tak' lub 'nie'.")
 
 
def main():
    menu_option = menu()
 
    while menu_option != 'koniec':
        if menu_option == 'nowa_gra':
            name = name_of_player()   
            gorny, dolny = choose_range()
            max_prob = difficulty_level()
            poziom = "łatwy" if max_prob is None else "średni" if max_prob == 10 else "trudny"
            gra(dolny, gorny, max_prob, poziom, name)
            play_again()
 
        menu_option = menu() 
 
if __name__ == "__main__":
    main()
 