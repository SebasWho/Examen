import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Parcial",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS REGISTRO")

sql = """CREATE TABLE REGISTRO(
        NOMBRE TEXT,
        EDAD   INT,
        PESO    FLOAT,
        ALTURA  FLOAT,
        FECHA   TEXT,
        HORA    TEXT
        );"""
cursor.execute(sql)
conn.commit()

while 'true':
    try:
        print('----------------------------------------------------------------------------------')
        print('----------------------------------------------------------------------------------')
        print("BIENVENIDOS AL SISTEMA DE NUESTRA CLINICA")
        print("1. REGISTRARSE ")
        print("2. CONSULTAR FECHAS PARA LAS CITAS")
        print("3. CITAS PROGRAMADAS")
        print("4. SALIR")
        print('----------------------------------------------------------------------------------')
        print('----------------------------------------------------------------------------------')
        opcion=int(input("INGRESE LA OPCION QUE DESEA: "))

        if opcion == 1:
            print("-------------REGISTRO DE PACIENTES-----------")
            nombre = str(input("INGRESAR SU NOMBRE: "))
            edad = int(input("INGRESAR SU EDAD: "))
            peso = float(input("INGRESAR SU PESO:  "))
            altura = float(input("INGRESAR SU ALTURA:  "))
            fecha = str(input("INGRESE LA FECHA DE SU CITA:  "))
            hora = str(input("INGRESE LA HORA DE LA CITA:  "))
            sql_insert_query = """ INSERT INTO REGISTRO(NOMBRE,EDAD, PESO, ALTURA,FECHA,HORA) VALUES (%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (nombre, edad,peso,altura,fecha,hora)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
        elif opcion ==2:
            print("-------------CONSULTAS DE LAS CITAS----------------")
            dia = str(input("INGRESE EL DIA QUE DESEA CONSULTAR: "))
            cursor.execute("SELECT NOMBRE,EDAD, PESO, ALTURA,FECHA,HORA FROM REGISTRO WHERE FECHA= %(dia)s",{'dia':dia})
            REGISTRO = cursor.fetchall()
            for i in REGISTRO:
                print(i)
        elif opcion == 3:
            print("---------------MOSTRANDO BITACORA------------------")
            cursor.execute("SELECT NOMBRE,EDAD, PESO, ALTURA,FECHA,HORA FROM REGISTRO")
            REGISTRO = cursor.fetchall()
            for i in REGISTRO:
                print(i)
        elif opcion == 4:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except:
        print('Se ha producido un error revisar los datos ingresados')