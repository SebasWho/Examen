import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS CUARTO")

sql = """CREATE TABLE CUARTO(
        ID INT,
        CONTEO INT
       )"""
cursor.execute(sql)
id = 0
while 'true':
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar Valores")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))

        if opcion == 1:
            V1 = int(input("Introduzca el primer valor: "))
            V2 = int(input("Intruduzca el segundo valor: "))

            if V1<V2:
                print('Mostrando intervalo')
                for i in range(V2,V1-1,-1):
                    id = id + 1
                    print(i , end=" "+' ')
                    archivo.write("Mostrando conteo: " + str(i)+'n')
                    sql_insert_query = """ INSERT INTO SEGUNDO(ID,CONTEO) VALUES (%s,%s)"""
                    record_to_insert = (id, i)
                    cursor.execute(sql_insert_query, record_to_insert)
                    count = cursor.rowcount
                    conn.commit()
                print()
            elif V2<V1:
                print('Mostrando intervalo')
                for i in range(V1, V2-1, -1):
                    print(i, end=" " + ' ')
                    id=id+1
                    archivo.write("Mostrando conteo: " + str(i)+'\n')
                    sql_insert_query = """ INSERT INTO CUARTO(ID,CONTEO) VALUES (%s,%s)"""
                    record_to_insert = (id,i)
                    cursor.execute(sql_insert_query, record_to_insert)
                    count = cursor.rowcount
                    conn.commit()


                print()

        elif opcion ==2:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            archivo.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')