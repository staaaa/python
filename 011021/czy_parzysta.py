def czy_parzysta(pesel):
    b = int(pesel[9])
    if b%2==0:
        return True
    else: 
        return False