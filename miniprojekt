biblioteka = [
    {"tytul": "Wiedźmin: Ostatnie życzenie", "autor": "Andrzej Sapkowski", "liczba_egzemplarzy": 5},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "liczba_egzemplarzy": 8},
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "liczba_egzemplarzy": 2},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "liczba_egzemplarzy": 6},
    {"tytul":"Miasteczko Middlemarch","autor":"George Eliot", "liczba_egzemplarzy":55},
    {"tytul":"Juda nieznany","autor":"Thomas Hardy", "liczba_egzemplarzy":45},
    {"tytul":"Oliver Twist","autor":"Charles Dickens", "liczba_egzemplarzy":51},
    {"tytul":"Germinal","autor":"Emile Zola", "liczba_egzemplarzy":42},
    {"tytul":"Pani Bovary ","autor":"Gustave Flaubert", "liczba_egzemplarzy":86},
    {"tytul":"Mały Książę","autor":"Antoine De Saint-Exupery", "liczba_egzemplarzy":98},
    {"tytul":"Trzej muszkieterowie","autor":"Alexandre Dumas", "liczba_egzemplarzy":21},
    {"tytul":"Hamlet","autor":"William Shakespeare", "liczba_egzemplarzy":21},
    {"tytul":"Fabryka os","autor":"Iain Banks", "liczba_egzemplarzy":23},
    {"tytul":"Opowieść wigilijna","autor":"Charles Dickens", "liczba_egzemplarzy":53},
    {"tytul":"Nędznicy","autor":"Victor Hugo", "liczba_egzemplarzy":63},
    {"tytul":"Pięć osób, które spotykamy w niebie","autor":"Mitch Albom", "liczba_egzemplarzy":56},
    {"tytul":"Okruchy dnia","autor":"Kazuo Ishiguro", "liczba_egzemplarzy":12},
    {"tytul":"Kolor purpury ","autor":"Alice Walker", "liczba_egzemplarzy":96},
    {"tytul":"Opętanie","autor":"AS Byatt", "liczba_egzemplarzy":31},
    {"tytul":"Ulisses","autor":"James Joyce", "liczba_egzemplarzy":73},
]
 
 
def dodaj_ksiazke(tytul, autor, liczba_egzemplarzy): #tworzy nowy słwonik i dodaje go do listy 
    nowa_ksiazka = {"tytul": tytul, "autor": autor, "liczba_egzemplarzy": liczba_egzemplarzy}
    biblioteka.append(nowa_ksiazka)
    print(f"Dodano książkę: {tytul} ({autor}) - {liczba_egzemplarzy} egzemplarzy")
 
def sortuj_ksiazki():
    return sorted(biblioteka, key=lambda ksiazka: ksiazka["liczba_egzemplarzy"], reverse=True)#labda złuzy do okreslenia klucz sortowania
 
 
def wyszukaj_ksiazke(szukany_tekst):
    znalezione = [ksiazka for ksiazka in biblioteka if szukany_tekst.lower() in ksiazka["tytul"].lower() or szukany_tekst.lower() in ksiazka["autor"].lower()]
    return znalezione  #szuka nam op tytule autorze i liczbie ekzeplarzy
 
def wyswietl_ksiazki():
    print("\nLista książek w bibliotece:")
    for ksiazka in sortuj_ksiazki():
        print(f"{ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['liczba_egzemplarzy']} egz.)")#petla po zegregowanej listcie i je zapisuje
 

dodaj_ksiazke("Zbrodnia i kara", "Fiodor Dostojewski", 3)# 
wyswietl_ksiazki()#
 #                                                                                           wywołuje funkcje
 #
szukany_tytul = "Hobbit"#
wyniki = wyszukaj_ksiazke(szukany_tytul)#
print(f"\nWyniki wyszukiwania dla '{szukany_tytul}':")#
for ksiazka in wyniki:#
    print(f"{ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['liczba_egzemplarzy']} egz.)") #
