#1. Trasformare cicli in list comprehension
## Fai tre esempi di cicli producono una lista e poi riscrivi lo stesso codice usando la list comprehension

##a - lista dei numeri pari da 0 a 14
pari = []
for n in range(15):
    if n%2 == 0:
        pari.append(n)
pariC = [n for n in range(15) if n%2==0]

print(pari)
print(pariC)


##b - lista con le stringhe più piccole di 5 caratteri di una lista di stringhe

stringhe = ["ciao", "arcobaleno", "gatto", "ape", "pace", "mano", "bicchiere" ]
minDi5 = []
for s in stringhe:
    if len(s) < 5:
        minDi5.append(s)
minDi5C = [s for s in stringhe if len(s) < 5]

print(minDi5)
print(minDi5C)

##c - lista dei cubi dei numeri da 0 a 9

cubi = []
for n in range(10):
    cubi.append(n**3)
cubiC = [n**3 for n in range(10)]

print(cubi)
print(cubiC)



