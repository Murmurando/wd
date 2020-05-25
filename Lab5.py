class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def zad6():
    tekst=Wspak("Nie pytają cię o imię walcząc z ostrym cieniem mgły")
    for litera in tekst:
        print(litera)

    lista=Wspak([12,42,51,2,215,125,1])
    for cyfra in lista:
            print(cyfra)

    krotka=Wspak((1,10,'kajak','hotel'))
    for x in krotka:
        print(x)

class parzysta:
    """Iterator zwracający parzyste wyrazy"""
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.stop = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.stop:
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index]

def zad7():
    tekst=parzysta("Kajak Krzysztof")
    print(next(tekst))
    print(next(tekst)) 
    print(next(tekst))   
    
class samogloska:
    """Iterator zwracający samogloski z wyrazenia"""
    def __init__(self, data):
        if isinstance(data,str):
            self.data = data
            self.index = 0
            self.stop = len(data)-1
        else:
            return None

    def __iter__(self):
        return self
    samogloski=['A','a','Ą','ą','E','e','Ę','ę','I','i','O','o','Ó','ó','U','u','Y','y']
    def __next__(self):
        if self.index >= self.stop:
            raise StopIteration
        while self.data[self.index] not in self.samogloski:
            #print(self.data[self.index])
            self.index = self.index + 1
        wynik = self.data[self.index]
        self.index = self.index + 1
        return wynik

def zad8():
    tekst=samogloska('Suma podstawy równa się kwadratowi obu ramion')
    for x in tekst:
        print(x)
 
def generator_na_wspak(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

def zad9():
    tekst=generator_na_wspak("Kiedyś było lepiej")
    


import itertools

def icotera(data):
    for element in itertools.combinations(data,3):
        yield element

def zad10():
    liczby=icotera('0123456789')
    for x in liczby:
        print(x)

def ciagF(x):
    c,i=(0,1)
    for _ in range(x):
        yield c
        c,i=(i,c+i)

def zad11():
    ciag=ciagF(10)
    print(list(ciag))

def zad12():
    import locale
    import datetime
    locale.setlocale(locale.LC_ALL, '')
    miesiace=[datetime.date(1900, x, 1).strftime('%B') for x in range(1,13,1)]
    print(miesiace)


#zad6()
#zad7()
#zad8()
#zad9()
#zad10()
#zad11()
#zad12()