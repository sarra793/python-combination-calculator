#Calcul du nombre de combinaisons
def saisir():
    n = int(input('n = '))
    ok = False
    while ok == False:
        p = int(input('p = '))
        ok = (1 <= p <= n)
    return n, p

def fact(x):
    f = 1
    for i in range(2, x + 1):
        f = f * i
    return f

def calculer(n, p):
    c = fact(n) // (fact(p) * fact(n - p))
    return c

# Programme principal
n, p = saisir()
cnp = calculer(n, p)
print('C(n,p) =', cnp)