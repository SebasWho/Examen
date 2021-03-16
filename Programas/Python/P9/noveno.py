import psycopg2
import math
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS NOVENO")

sql = """CREATE TABLE NOVENO (
        ID INT,
        RESULTADO FLOAT
       )"""
cursor.execute(sql)
id=0

while 'true':
    id = id + 1
    resul=0
    b=0
    h=0

    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Calcular area del Circulo")
        print("2. Calcular area del Triangulo")
        print("3. Calcular area del Cuadrado")
        print("4. Calcular area del Rectangulo")
        print("5. Mostrar historial")
        print("6. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:

            print('A escogido calcular el area de un circulo')
            V1 = float(input("Introduzca el radio: "))
            resul= math.pi * (V1 ** 2)
            print('El area del circulo es: ', resul)

            archivo.write('El area del circulo es: '+ str(resul) + '\n')
            sql_insert_query = """ INSERT INTO NOVENO(ID,RESULTADO) VALUES (%s,%s)"""
            record_to_insert = (id, resul)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif opcion == 2:
            print('A escogido calcular el area de un Triangulo')
            b = float(input("Introduzca la base: "))
            h=float(input('Introduzca la altura: '))
            resul = (b*h)/2
            print('El area del triangulo es: ', resul)
            archivo.write('El area del triangulo es: ' + str(resul) + '\n')
            sql_insert_query = """ INSERT INTO NOVENO(ID,RESULTADO) VALUES (%s,%s)"""
            record_to_insert = (id, resul)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif opcion == 3:
            print('A escogido calcular el area de un cuadrado')
            b = float(input("Introduzca la base: "))
            resul = b*b
            print('El area del cuadrado es: ', resul)
            archivo.write('El area del cuadrado es: ' + str(resul) + '\n')
            sql_insert_query = """ INSERT INTO NOVENO(ID,RESULTADO) VALUES (%s,%s)"""
            record_to_insert = (id, resul)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif opcion == 4:
            print('A escogido calcular el area de un rectangulo')
            b = float(input("Introduzca la base: "))
            L = float(input("Introduzca el lado: "))
            resul = b * L
            print('El area del rectangulo es: ', resul)
            archivo.write('El area del rectangulo es: ' + str(resul) + '\n')
            sql_insert_query = """ INSERT INTO NOVENO(ID,RESULTADO) VALUES (%s,%s)"""
            record_to_insert = (id, resul)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif opcion ==5:
                cursor.execute("SELECT ID, RESULTADO FROM NOVENO;")
                NOVENO= cursor.fetchall()
                for i in NOVENO:
                    print(i)
        elif opcion ==6:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            archivo.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')