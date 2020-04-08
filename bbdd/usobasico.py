import sqlite3 as dbapi

print dbapi.apilevel
print dbapi.threadsafety
print dbapi.paramstyle

bbdd = dbapi.connect("bbdd.dat")
print bbdd

# las distintas operaciones que podemos realizar con la base de datos se realizan a traves de un objeto curson
# para crear este objeto se utilza el metodo cursor() del objeto connection:

c = bbdd.cursor()       #         -.-'
                        #          -
                        
# crear una nueva tabla empleados en la base de datos
# c.execute("""create table empleados (dni text, nombre text, departament text)""")

# insertamos una tupla en nuestra tabla
c.execute("""insert into empleados values ('4624902-Q','Xiang Lu', 'Student')""")
                       
