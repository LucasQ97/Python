import Database
from mysql.connector import errorcode
from mysql.connector.errors import Error

def leer(con):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM mesas')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

leer(Database.con)


def insertar(con):
    cursoObj= con.cursor()
    try:
        cursoObj.execute('INSERT INTO `mesas`(`descripcion`, `cant_personas`, `reserva_entrada`, `reserva_salida`, `estado`, `FECHA`) VALUES ("MESA2",2,"22:00","00:00","OCUPADO","2020-11-28")')
        print('entro como piña')
        con.commit()
        print(cursoObj.rowcount, "Record inserted successfully into Laptop table")
        cursoObj.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))

    finally:
        if (con.is_connected()):
            con.close()
            print("MySQL connection is closed")

insertar(Database.con)