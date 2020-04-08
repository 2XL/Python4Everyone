l =[1,2,3]

# el operaddor lambda sirve para crear funciones anonimas, sin nombre
# no pueden ser referenciadas

l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)
print l2
def es_par(n):
    return (n % 2.0 == 0)
l = [1, 2, 3]
l2 = filter(es_par, l)
print l2