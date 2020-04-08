


# map(func,seq[,seq,..])

def cuadrado(n):
    return n**2

l = [1,2,3,4,5,6,7,8,9,10]
ll= map(cuadrado, l)

print ll

# filter(func,seq)


def es_par(n):
    return (n%2.0==0)
lf=filter(es_par,l)
print lf

# reduce (func,seq[,initial])

def sumar(x,y):
    return x+y

ls=reduce(sumar, l)
print ls