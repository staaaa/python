pkt = int(input("Podaj liczbe zdobytych punktów przez klasę: "))
f = float(input("Podaj frekwencje klasy: "))
so = float(input("Podaj średnią ocen klasy: "))

if f>94 and so>=4.0:
    pkt+=20
print("Aktualna liczba punktow wynosi "+str(pkt))