import sys
print("podaj tekst")
s = sys.stdin.readline()
print (s.count(" "))

a = int(input("podaj liczbe "))
b= int(input("podaj liczbe "))
iloczyn=a*b
print(iloczyn)

c = int(input("podaj liczbe "))
print(abs(c))

a = int(input("podaj liczbe a "))
b = int(input("podaj liczbe b "))
c = int(input("podaj liczbe c "))
if 0<a<10:
    print("liczba a jest w przedziale od 0 do 10")
else:
    print("liczba a nie jest w przedziale od 0 do 10")
if a>b:
    print("liczba a jest wieksza od liczby b")
else:
    print("liczba b jest wieksza od a")
if b>c:
    print("liczba b jest wieksza od liczby c")
else:
    print("liczba c jest wieksza od b")
    
 for x in range(1,100,1):
    if x%5==0:
        print(str(x) + " ")
        
a = int(input("Ile chcesz podac liczb? "))
for a in range(0,a,1):
    b=int(input("Podaj liczbe: "))
    print(b**2)
    
z = int(input("Podaj liczbe, 0 konczy dodawnie liczb do listy: "))
while(z!=0):
    z = int(input("Podaj liczbe, 0 konczy dodawnie liczb do listy: "))
    z in lista
    print(str(z) + " ")

z=input('Podaj liczbę\n')
i=0
suma=0
while i < len(z):
    suma+=int(z[i])
    1i+=1
    print(suma)
    
a=int(input("Podaj wielkość wieży: "))
if a<11:1
    for i in range(a):
        print('A' *i)
        
a=int(input("Podaj wielkość wieży diamentów: "))
mid=int((a+1)/2)
for x in range(1,a+1,1):
    print('{:^10}'.format('o'*(2*(mid-abs(mid-x))-1)))
    
a=list(range(1,11,1))
print('  x  ', end='')
for i in a:
    print ('{:^5}'.format(a[i-1]), end='')
    print('\n')
for i in a:
        print ('{:^5}'.format(i), end='')
        for j in a:
            print ('{:^5}'.format(a[j-1]*i), end='')
        print('\n')
        
import math
a=input('Proszę podać liczbę do obliczenia pierwiastka\n')
try:
    print('Pierwiastek z ' + a +' to ' +str(math.sqrt(int(a))))
except ValueError:
    print('Ta funkcja nie liczy pierwiastków z liczb ujemnych')
