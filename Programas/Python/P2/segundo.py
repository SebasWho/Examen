import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS SEGUNDO")

sql = """CREATE TABLE SEGUNDO(
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
        print("1. Ingresar rangos")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))

        if opcion == 1:
            li = int(input("Introduzca el rango inferior: "))
            lf = int(input("Intruduzca el limite superior: "))

            if lf<=li:
                print("Error el limite superior no puede ser menor que el inferior")

            else:
                print("Mostrando el conteo")

                for i in range(li, lf+1,2):

                    print(i , end=" "+' ')
                    id=id+1
                    archivo.write("Mostrando conteo: " + str(i)+'\n')
                    sql_insert_query = """ INSERT INTO SEGUNDO(ID,CONTEO) VALUES (%s,%s)"""
                    record_to_insert = (id,i)
                    cursor.execute(sql_insert_query, record_to_insert)
                    count = cursor.rowcount
                    conn.commit()


                print()

        elif opcion ==2:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')