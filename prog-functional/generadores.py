
l =[1,2,3]






l2 = (n ** 2 for n in l)

print l2

l2 = [n ** 2 for n in l]

print l2



def mi_gen(n,m,s):
    while(n<=m):
        yield n
        n+=s
        
x = mi_gen(0, 5, 1)
print x


for n in mi_gen(0, 5, 1):   # sirve fundamentalmente para ahorar memoria
    print n                 # ya que solo guarda una formula i no una lista en memoria ara recorrer

lista = list(mi_gen(0,10,2))
print lista

