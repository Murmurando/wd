def zad1():
    lista=[x for x in range(1,100)if x%4==0]
    plik = open("podzielne_przez_4.txt","w")
    plik.write(str(lista))

def zad2():
    with open("podzielne_przez_4.txt", "r") as plik:
        for linia in plik:
            print(linia, end="")

def zad3():
    with open("tekst.txt", "a+") as plik:
        plik.write("Programowanie obiektowe wymaga zaprojektowania struktury opartej na danych i kodzie. \nTaka struktura nazywana jest klasą a każdy obiekt stworzony na podstawie tej klasy to instancja instancją (albo wystąpieniem) danej klasy. \nDane powiązane z obiektem to będą atrybuty ( inaczej własności lub właściwości) a funkcje, które wykonują coś na obiekcie to metody.")
    with open("tekst.txt") as plik:    
        print(plik.readlines())
#zad1()
#zad2()
#zad3()