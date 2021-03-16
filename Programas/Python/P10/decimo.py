import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="Tareas",
    user="postgres",
    password="sebastian"
    )
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DECIMO")
sql = """CREATE TABLE DECIMO (
        ID INT,
        RESULTADO CHAR(100)
       )"""
cursor.execute(sql)
id=0
while 'true':
    id = id + 1
    resul=0
    b=0
    h=0
    archivo = open('Salida.txt', 'a')
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Ingresar los lados del triangulo")
        print("2. Mostrar historial")
        print("3. Salir del programa")
        opcion=int(input("Indique que opcion desea realizar: "))
        if opcion == 1:
            V1 = float(input("Introduzca el primer lado del triangulo: "))
            V2 = float(input("Introduzca el segundo lado del triangulo: "))
            V3 = float(input("Introduzca el tercer lado del triangulo: "))
            if V1==V2 and V2==V3:
                print('Es un triangulo Equilatero')
                archivo.write('Es un triangulo Equilatero'+'\n')
                sql_insert_query = """ INSERT INTO DECIMO(ID,RESULTADO) VALUES (%s,%s)"""
                record_to_insert = (id, 'Es un triangulo Equilatero')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            elif V1!=V2 and V2!=V3 and V1!=V3:
                print('Es un triangulo Escaleno')
                archivo.write('Es un triangulo Escaleno' + '\n')
                sql_insert_query = """ INSERT INTO DECIMO(ID,RESULTADO) VALUES (%s,%s)"""
                record_to_insert = (id, 'Es un triangulo Escaleno')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
            elif (V1!=V2 and V1==V3)or(V1==V2 and V1!=V3)or(V2==V3 and V2!=V1) :
                print('Es un triangulo Isosceles')
                archivo.write('Es un triangulo Isosceles' + '\n')
                sql_insert_query = """ INSERT INTO DECIMO(ID,RESULTADO) VALUES (%s,%s)"""
                record_to_insert = (id, 'Es un triangulo Isosceles')
                cursor.execute(sql_insert_query, record_to_insert)
                count = cursor.rowcount
                conn.commit()
                print()
        elif opcion ==2:
                cursor.execute("SELECT ID, RESULTADO FROM DECIMO;")
                DECIMO= cursor.fetchall()
                for i in DECIMO:
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