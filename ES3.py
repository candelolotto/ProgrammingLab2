import numpy as np

#3. Operazioni su array
##Crea un array a, 1D (senza digitarlo esplicitamente), e genera due nuovi array b, 
##contenente una sottostringa a piacere e c che è il reverse dell'array a (esempio [1,2,3] diventa [3,2,1]) . 
##Dividi l'array a per l'array c. Fai la stessa cosa per una lista.

lista = [i for i in range(1,6)]

a = np.array(lista)
print(a)
b = a[3:6]
print(b)
c = a[::-1]
print(c)
print(a/c)

aa = lista.copy()
print(aa)
bb = a[3:6]
print(bb)
cc = aa[::-1]
print(cc)
#print(aa/cc) -> da errore

divisione = [aa[i]/cc[i] for i in range(len(aa))]
print(divisione)