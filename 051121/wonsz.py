#zadanie 1
for i in range(2,10,2):
  print(i)

#zadanie 2
for i in range(50,150,3):
  print(i)

#zadanie 3
lista = [1,4,67,3,5,-1]
najmniejsza = lista[0]
for i in lista:
  if i < najmniejsza:
    najmniejsza = i
print(najmniejsza)  

#zadanie 4
for i in range(0,10,1):
  print(i)
  print(i+i-1)

#zadanie 5
for i in range(1,8):
  if i == 5:
    print("Znalazlem 5")
  else:
    print(i)

#zadanie 6
for i in range(1,4):
  for j in ["a", "b", "c"]:
    print(str(i)+j)

#zadanie 7
for i in range(10, -1,-1):
  if i != 0:
    print(i)
  else:
    print("RAKIETA STARTUJE")

#zadanie 8

lista1 = ["KKKK", "GGGG", "HHHH"]
lista2 = ["563-12", "363-AB"]

for i in lista1:
  for j in lista2:
    print(i+" "+j)
  print("-----------")