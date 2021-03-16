import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS TRECEAVO")
sql = """CREATE TABLE TRECEAVO (
        AÑO INT,
        DESCRIPCION CHAR(100)
       )"""
cursor.execute(sql)

while 'true':
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar año de nacimiento")
        print("2. Mostrar historial")
        print("3. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            V1 = int(input("Introduzca su año de nacimiento: "))
            if (V1%4==0)and((V1%100!=0)or(V1%400==0)):
                print('EL AÑO',V1,'FUE UN AÑO BISIESTO')
                archivo.write('EL AÑO'+str(V1)+'FUE UN AÑO BISIESTO'+'\n')
                sql_insert_query = """ INSERT INTO TRECEAVO(AÑO,DESCRIPCION) VALUES (%s,%s)"""
                record_to_insert = (V1, 'AÑO BISIESTO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            else :
                print('EL AÑO', V1, ' NO FUE UN AÑO BISIESTO')
                archivo.write('EL AÑO' + str(V1) + ' NO FUE UN AÑO BISIESTO''\n')
                sql_insert_query = """ INSERT INTO TRECEAVO(AÑO,DESCRIPCION) VALUES (%s,%s)"""
                record_to_insert = (V1, 'AÑO NO BISIESTO')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
        elif opcion ==2:
                print('Mostrando Historial.......')
                cursor.execute("SELECT AÑO,DESCRIPCION FROM TRECEAVO;")
                TRECEAVO= cursor.fetchall()
                for i in TRECEAVO:
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