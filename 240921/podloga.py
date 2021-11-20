import math

dlugosc = float(input("Podaj dlugosc prostokatnej podlogi: "))
szerokosc = float(input("Podaj szerokosc prostokatnej podlogi: "))
mkw = float(input("Podaj ile metrow kwadratowych mozna wylozyc z jednej paczki: "))

print(math.ceil(dlugosc*szerokosc/mkw))