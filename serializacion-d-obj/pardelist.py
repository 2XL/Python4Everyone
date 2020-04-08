





try:
    import cPickle as pickle
except ImportError:
    import pickle




fichero = file("datos.dat", "w")
animales = ["piton", "mono", "camello"]
lenguajes = ["python", "mono", "perl"]
pickle.dump(animales, fichero)
pickle.dump(lenguajes, fichero)
fichero = file("datos.dat")
animales2 = pickle.load(fichero)
lenguajes2 = pickle.load(fichero)
print animales2
print lenguajes2









