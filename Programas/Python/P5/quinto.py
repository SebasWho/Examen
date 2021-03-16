import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS QUINTO")

sql = """CREATE TABLE QUINTO(
        ID INT,
        VOCALES CHAR(100)
       )"""
cursor.execute(sql)
id = 0

while 'true':
    cont = 0
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar Palabra")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        id = id + 1
        if opcion == 1:
            palabra = str(input("Introduzca la palabra que desea: "))

            for i in palabra:
                if f'{i}'=='a' or f'{i}'=='e' or f'{i}'=='i' or f'{i}'=='o' or f'{i}'=='u' :
                    cont=cont+1
            print('La palabra '+palabra+' tiene: ',cont,' vocales')
            archivo.write('La palabra '+ palabra +' tiene: '+str(cont)+' vocales'+'\n')
            sql_insert_query = """ INSERT INTO QUINTO(ID,VOCALES) VALUES (%s,%s)"""
            record_to_insert = (id, cont)
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