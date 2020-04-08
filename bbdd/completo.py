import sqlite3 as dbapi


bbdd = dbapi.connect("bbdd.dat")
cursor = bbdd.cursor()
# cursor.execute("""create table empleados (dni text, nombre text,departamento text)""")
# cursor.execute("""insert into empleados values ('12345678-A', 'Manuel Gil', 'Contabilidad')""")
bbdd.commit()

cursor.execute("""select * from empleados where departamento='Contabilidad'""")
for tupla in cursor.fetchall():
    print tupla
"""
for resultado in cursor:
    print resultado
"""
""" 
para realizar consultas a la bd tambien se utiliza execute
    las consultas resultantes se tiene que parchearlo
    con los metodos:
        cursor
            fetchone        - una tupla
            fetchmany(num)    - num indicado de tuplas (o predefinido por : Cusor.arraysize (defecto : 1))
            fetchball - con todas las tuplas! objeto iterable
"""
cursor.close()
bbdd.close()

"""

existen bd realacionales 
i 
bd realacionados a objetos

"""