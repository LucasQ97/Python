import mysql.connector

def creardb():
    try:
        conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin")
        con = conexion.cursor()
        con.execute("CREATE DATABASE IF NOT EXISTS sistemareservas")
        print('Se creo la base de datos')
        conexion = mysql.connector.connect(
            host="localhost", user="root", passwd="admin", database="sistemareservas")
        con = conexion.cursor()
        con.execute("CREATE TABLE IF NOT EXISTS MESAS( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, MESA VARCHAR(10) COLLATE utf8_spanish2_ci NOT NULL, CANT_PERSONAS int(11) NOT NULL, RESERVA VARCHAR(5) COLLATE utf8_spanish2_ci NOT NULL, FECHA VARCHAR(20) COLLATE utf8_spanish2_ci NOT NULL , NOMBRE VARCHAR(20) COLLATE utf8_spanish2_ci NOT NULL )")
        print('Se creo la tabla MESAS')
    except:
        print("La base de datos ya existe")


def conectar():
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="admin", database="sistemareservas")
        return con
    except:
        print('error al conectar con DB')

def drop():
    try:
        conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin",database="sistemareservas")
        con = conexion.cursor()
        con.execute("DROP DATABASE IF EXISTS sistemareservas")
        print("La base de datos ya NO existe")
    except:
        print("La base de datos NO existe")
        