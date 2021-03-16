import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS OCTAVO")
sql = """CREATE TABLE OCTAVO(
        ID INT,
        IMPARES INT
       )"""
cursor.execute(sql)
id=0
while 'true':
    cont=0

    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Calcular los numeros impares de 1 a 100")
        print("2. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            print('Calculando los numeros impares......')
            archivo.write('Los numeros impares de 1 a 100 son: '+'\n')
            for i in range(1,101):
                if i%2!=0:
                    id = id + 1
                    print(i)
                    cont=cont+1
                    archivo.write(str(i)+'\n')
                    sql_insert_query = """ INSERT INTO OCTAVO(ID,IMPARES) VALUES (%s,%s)"""
                    record_to_insert = (id,i)
                    cursor.execute(sql_insert_query, record_to_insert)
                    count = cursor.rowcount
                    conn.commit()
                    print()
            print('Del 1 al 100 hay ',cont,' numeros impares')
            archivo.write('Del 1 al 100 hay '+str(cont)+' numeros impares'+ '\n')
        elif opcion ==2:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            archivo.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')