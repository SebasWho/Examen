import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DOCEAVO")
sql = """CREATE TABLE DOCEAVO (
        NUMERO INT,
        FACTORIAL NUMERIC
       )"""
cursor.execute(sql)

while 'true':
    archivo = open('Salida.txt', 'a')
    resultado = 1
    i = 1
    print('----------------------------------------------------------------------------------')
    #try:
    print("Bienvenidos al sistema")
    print("1. Calcular factorial")
    print('2. Mostrar Historial')
    print("3. Salir")
    opcion=int(input("Indique que opcion desea realizar: "))

    if opcion == 1:
        print("Cual es el valor del cual desea el factorial ")
        fac=int(input())
        if fac<0:
            print("Error, no se puede calcular el factorial de un número negativo")
        else:
            if fac%7==0:
                for i in range(1,fac+1):
                    resultado=resultado*i
                archivo.write('El factorial de '+ str(fac)+' es'+str(resultado)+'\n')
                archivo.close()
                print('El factorial de ', fac, 'es', resultado)
                sql_insert_query = """ INSERT INTO DOCEAVO(NUMERO,FACTORIAL) VALUES (%s,%s)"""
                record_to_insert = (fac, resultado)
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()

            else:
                print('Error, el valor ingresado no es diferencial de 7')
    elif opcion==2:
        print('Mostrando Historial.......')
        cursor.execute("SELECT NUMERO, FACTORIAL FROM DOCEAVO;")
        DOCEAVO = cursor.fetchall()
        for i in DOCEAVO:
            print(i)
    elif opcion ==3:
        print("Gracias por utilizar nuestro sistema")

        break
    else:
        print('No se ingreso ninguna de las opciones vuelva a intentarlo')
        #except :
     #   print('Se ha producido un error revisar los datos ingresados')