#zadanie 1
def zadanie1():
  i = 2
  while i < 9:
    print(i)
    i+=1
zadanie1()

print("-----------")

#zadanie 2
def zadanie2(lista):
  for i in lista:
    print(i)
zadanie2([1,2,45,6,78,9])

print("-----------")

#zadanie 3
def zadanie3(lista,znak):
  for i in lista:
    if i == znak:
      print("Znaleziono znak " + znak)
      break;
    else:
      print(i)
zadanie3("Stachu",'u')