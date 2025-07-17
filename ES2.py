import numpy as np

# 2. Vettore di Numeri Primi
##Crea un vettore contenente tutti i numeri primi compresi tra 0 e 10
##(Puoi scriverli direttamente nell'array).

primi = np.array([2, 3, 5, 7])

##Conta quanti numeri ci sono nel vettore utilizzando la funzione len(). Ottieni lo stesso numero accedendo all'attributo .size del vettore.

print(len(primi))
print(primi.size)

##Quale pensi sia il tipo di dato (dtype) del vettore? Prova a rispondere senza eseguire il codice e Verifica la tua risposta accedendo all'attributo .dtype del vettore
#penso che sarà di tipo intero
print(primi.dtype)
##Scrivi l'array usando una list comprehension che controlla che i numeri siano primi.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 
primiC = np.array([i for i in range(11) if is_prime(i)])

print(primiC)