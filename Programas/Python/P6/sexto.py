import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS SEXTO")

sql = """CREATE TABLE SEXTO(
        A INT,
        E INT,
        I INT,
        O INT,
        U INT
       )"""
cursor.execute(sql)

while 'true':
    a = 0
    e=0
    I=0
    o=0
    u=0
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar Palabra")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            palabra = str(input("Introduzca la palabra que desea: "))

            for i in palabra:
                if f'{i}'=='a':
                    a=a+1
                elif f'{i}'=='e':
                    e=e+1
                elif f'{i}'=='i':
                    I=I+1
                elif f'{i}'=='o':
                    o=o+1
                elif f'{i}'=='u':
                    u=u+1
            print('A=',a,'E=',e,'I=',I,'O=',o,'U=',u)
            archivo.write(' A='+str(a)+' E='+str(e)+' I='+str(I)+' O='+str(o)+' U='+str(u)+'\n')
            sql_insert_query = """ INSERT INTO SEXTO(A,E,I,O,U) VALUES (%s,%s,%s,%s,%s)"""
            record_to_insert = (a,e,I,o,u)
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