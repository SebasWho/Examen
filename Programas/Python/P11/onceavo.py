import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ONCEAVO")
sql = """CREATE TABLE ONCEAVO (
        PROMEDIO FLOAT,
        CALIFICACION CHAR(100)
       )"""
cursor.execute(sql)

while 'true':
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar Notas")
        print("2. Mostrar historial")
        print("3. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            V1 = float(input("Introduzca el primera nota: "))
            V2 = float(input("Introduzca el segunda nota: "))
            V3 = float(input("Introduzca el tercera nota: "))
            Promedio=(V1+V2+V3)/3
            print('El promedio es: ', Promedio)
            if Promedio>=60:
                print('*********APROBADO*********')
                archivo.write('El promedio es: ' + str(Promedio) + '\n')
                archivo.write('*********APROBADO*********' + '\n')
                sql_insert_query = """ INSERT INTO ONCEAVO(PROMEDIO,CALIFICACION) VALUES (%s,%s)"""
                record_to_insert = (Promedio, 'APROBADO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            elif  Promedio<60:
                print('*****REPROBADO****')
                archivo.write('El promedio es: '+str(Promedio) + '\n')
                archivo.write('*****REPROBADO****' + '\n')
                sql_insert_query = """ INSERT INTO ONCEAVO(PROMEDIO,CALIFICACION) VALUES (%s,%s)"""
                record_to_insert = (Promedio, 'REPORBADO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
        elif opcion ==2:
                print('Mostrando Historial.......')
                cursor.execute("SELECT PROMEDIO, CALIFICACION FROM ONCEAVO;")
                ONCEAVO= cursor.fetchall()
                for i in ONCEAVO:
                    print(i)
        elif opcion ==3:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            archivo.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')