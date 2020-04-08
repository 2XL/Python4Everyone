
try:
    import cPickle as pickle
except ImportError:
    import pickle
fichero = file("datos2.dat", "w")
animales = ["piton", "mono", "camello" ]
pickle.dump(animales, fichero, 2)
fichero.close()