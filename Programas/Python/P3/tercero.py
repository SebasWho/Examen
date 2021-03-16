import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS TERCERO")

sql = """CREATE TABLE TERCERO(
        ID INT,
        DIVISORES INT
        )"""
cursor.execute(sql)
Id=0
while 'true':
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Obtener los divisores")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            print("Introduzca el valor del cual desea calcular los divisores")
            V1 = int(input())
            print("Calculando......")
            print('Los divisores de ',V1,'son: ')
            for i in range(1,V1+1):
                if V1 % i==0:
                    Id = Id + 1
                    print(i , end=" "+' ')
                    archivo.write('Los divisores de '+str(V1)+ ' son: ' + str(i) + '\n')
                    sql_insert_query = """ INSERT INTO TERCERO(ID, DIVISORES) VALUES (%s,%s)"""
                    record_to_insert = (Id,i)
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
