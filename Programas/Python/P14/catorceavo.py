import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CATORCEAVO")
sql = """CREATE TABLE CATORCEAVO (
        MODELO INT,
        KILOMETRAJE INT,
        ESTADO CHAR(100)
       )"""
cursor.execute(sql)
while 'true':
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar Datos del Automovil")
        print("2. Mostrar historial")
        print("3. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            V1 = int(input("Ingrese el modelo del Automovil: "))
            V2 = int(input("Ingrese los kilometros que lleva recorrido: "))
            if (V1<2007) and V2>20000:
                print('El Automovil Modelo ',V1,' debe renovarse')
                archivo.write('El Automovil Modelo '+str(V1)+ ' debe renovarse' + '\n')
                sql_insert_query = """ INSERT INTO CATORCEAVO(MODELO,KILOMETRAJE,ESTADO) VALUES (%s,%s,%s)"""
                record_to_insert = (V1,V2 ,'RENOVARSE')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            elif  V1>=2007 and V1<=2013 and V2==20000:
                print('El automovil modelo',V1,' debe recibir mantenimiento')
                archivo.write('El automovil modelo '+str(V1)+' debe recibir mantenimiento'+ '\n')
                sql_insert_query = """ INSERT INTO CATORCEAVO(MODELO,KILOMETRAJE,ESTADO) VALUES (%s,%s,%s)"""
                record_to_insert = (V1,V2, 'MANTENIMIENTO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            elif V1 >2013 and V2 < 10000:
                print('El automovil modelo', V1, ' esta en optimas condiciones')
                archivo.write('El automovil modelo ' + str(V1) + ' esta en optimas condiciones' + '\n')
                sql_insert_query = """ INSERT INTO CATORCEAVO(MODELO,KILOMETRAJE,ESTADO) VALUES (%s,%s,%s)"""
                record_to_insert = (V1, V2, 'OPTIMAS CONDICIONES')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            else:
                print('MECANICO')
                archivo.write('MECANICO' + '\n')
                sql_insert_query = """ INSERT INTO CATORCEAVO(MODELO,KILOMETRAJE,ESTADO) VALUES (%s,%s,%s)"""
                record_to_insert = (V1, V2, 'MECANICO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
        elif opcion ==2:
                print('Mostrando Historial.......')
                cursor.execute("SELECT MODELO, KILOMETRAJE, ESTADO FROM CATORCEAVO;")
                CATORCEAVO= cursor.fetchall()
                for i in CATORCEAVO:
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