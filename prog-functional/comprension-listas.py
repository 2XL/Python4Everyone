l =[1,2,3]
l2 = [n ** 2 for n in l]
print l2

l2 = [n for n in l if n % 2.0 == 0]
print l2

l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v 
     for s in m
        for v in l
            if v > 0]
print n

n = []
for s in m:
    for v in l:
        if v > 0:
            n.append(s* v)

print n