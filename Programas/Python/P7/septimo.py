import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS SEPTIMO")

sql = """CREATE TABLE SEPTIMO(
        ID INT,
        RESULTADO INT
       )"""
cursor.execute(sql)

while 'true':
    resul=0
    id=0
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Calculo de la sumatoria")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        id = id + 1
        if opcion == 1:
            V1 = int(input("Introduzca el valor que desee: "))

            for i in range(1,V1+1):
                resul=resul+i
            print('El resultado de la sumatoria hasta el numero: ',V1,'es: ',resul)
            archivo.write('El resultado de la sumatoria hasta el numero: '+str(V1)+' es: '+str(resul)+'\n')
            sql_insert_query = """ INSERT INTO SEPTIMO(ID,RESULTADO) VALUES (%s,%s)"""
            record_to_insert = (id,resul)
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