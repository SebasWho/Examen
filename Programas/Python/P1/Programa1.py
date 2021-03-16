import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS PRIMERO")
sql = """CREATE TABLE PRIMERO(
        SUMA FLOAT,
        MULTIPLICACION  FLOAT ,
        CONCATENAR  CHAR(100),
        DISTINTO FLOAT,
        IGUALES  CHAR(100)
        )"""
cursor.execute(sql)
while 'true':
    archivo = open('Salida.txt', 'a')
    resultado = 0
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar valores a comparar")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))

        if opcion == 1:
            print("Introduzca los 3 valores a comparar")
            V1 = float(input())
            V2 = float(input())
            V3 = float(input())
            if V1>V2 and V1>V3 and V3!=V1 and V2!=V1 and V2!=V3:
                print("Efectuando la suma de los tres valores")
                resultado=V1+V2+V3
                archivo.write("Efectuando la suma de los tres valores: " + str(resultado) + '\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO,IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (resultado,0,0,0,'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()

                print(resultado)
            elif V2>V1 and V2>V3 and V3!=V1 and V2!=V1 and V2!=V3:
                print("Efectuando la multiplicación de los tres valores")
                resultado = V1 * V2 * V3
                archivo.write("Efectuando la multiplicación de los tres valores: " + str(resultado) + '\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO,IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0, resultado, 0,0, 'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print(resultado)
            elif V3>V1 and V3 > V2 and V3!=V1 and V2!=V1 and V2!=V3:
                print("Efectuando la concatenacion")
                archivo.write("Efectuando la concatenacion: " + str(V1) +str(V2)+str(V3)+ '\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO ,IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0, 0, str(V1)+str(V2)+str(V3),0, 'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print(V1,V2,V3)
            elif V1==V2 and V3!=V1:
                print('El Valor distinto es: ', V3)
                archivo.write('El Valor distinto es:'+ str(V3)+'\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO,IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0,0,0,V3, 'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
            elif V2==V3 and V3!=V1:
                print('El Valor distinto es: ', V1)
                archivo.write('El Valor distinto es:'+ str(V1)+'\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO, IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0, 0, 0, V1, 'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
            elif V1==V3 and V2!=V1:
                print('El Valor distinto es: '+ str(V2)+'\n')
                archivo.write('El Valor distinto es:'+ str(V2)+ '\n')
                archivo.close()
                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO, IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0, 0, 0, V2, 'DISTINTOS')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
            elif V1==V3 and V2==V1:
                print("Estos fueron los tres valores ingresados")
                print(V1)
                print(V2)
                print(V3)
                print("Todos son iguales")
                archivo.write("Estos fueron los tres valores ingresados: "+'\n')
                archivo.write(str(V1) + '\n')
                archivo.write(str(V2) + '\n')
                archivo.write(str(V3) + '\n')
                archivo.write("Son iguales" + '\n')
                archivo.close()

                sql_insert_query = """ INSERT INTO PRIMERO(SUMA,MULTIPLICACION,CONCATENAR,DISTINTO,IGUALES) VALUES (%s,%s,%s,%s,%s)"""
                record_to_insert = (0, 0, 0,0, 'SON IGUALES')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
        elif opcion ==2:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')