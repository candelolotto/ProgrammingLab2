# 1)
## 1a
lista = []
for i in range(10):
    lista.append(i)

listaC = [i for i in range(10)]

print(lista)
print(listaC)

## 1b

pari = []
count = 0
i = 0
while count < 5:
    if i % 2 == 0 and i  % 3 == 0:
        pari.append(i)
        count += 1
    i += 1

pariC = [i for i in range(100) if i % 2 == 0 and i % 3 == 0][:5]

print(pari)
print(pariC)

## 1c 

elenco = ["albero", "casa", "matita", "bottiglia", "ape"]
lista = []
for elemento in elenco:
    if len(elemento) > 5:
        lista.append(elemento)

listaC = [elemento for elemento in elenco if len(elemento) > 5]

print(lista)
print(listaC)


# 2) vettore numeri primi
## 2a
import numpy as np

primi = []
for i in range(2, 11):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primi.append(i)

primi = np.array(primi)
print(primi)
