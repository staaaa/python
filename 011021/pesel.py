import czy_parzysta


a = str(input("Podaj swoj numer pesel: "))
if len(a) < 11 or len(a) > 11:
    print("Wprowadzony pesel jest niepoprawny")
elif czy_parzysta.czy_parzysta(a) == True:
    print("Jesteś Kobietą!")
else:
    print("Jesteś Mężczyzną :(")