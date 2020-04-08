

try:
    import cPickle as pickle
except ImportError:
    import pickle
    
fichero = file("datos1.dat", "w")
animales = ["piton", "mono", "camello"]
pickle.dump(animales, fichero, 1)
fichero.close()



fichero = file("datos1.dat")
animales2 = pickle.load(fichero)
print animales2