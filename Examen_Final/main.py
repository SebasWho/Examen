import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="Parcial",
    user="postgres",
    password="sebastian"
    )

cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS VUELOS")
sql = """CREATE TABLE VUELOS (
        USUARIO     TEXT,
        SUBTOTAL    FLOAT,
        DESCUENTO   TEXT,
        DESCUENTO1   FLOAT,
        TOTAL       FLOAT
        );"""
cursor.execute(sql)
conn.commit()
while 'true':
    try:
        print('----------------------------------------------------------------------------------')
        print("BIENVENIDO A NUESTRA VENTA DE BOLETOS")
        print("1. INGRESAR USUARIO")
        print("2. BITACORA")
        print("3. SALIR")
        opcion=int(input("CUAL DE LAS OPCIONES DESEA: "))
        print('----------------------------------------------------------------------------------')
        contador=0
        total3=0
        total1 = 0
        total2 = 0
        cont=0
        condicion=1
        m = 0
        n = 0
        o = 0
        if opcion == 1:
            print("************************* LOGIN *******************************")
            usuario=str(input("INGRESE SU NOMBRE DE USUARIO: "))
            contraseña= str(input("INGRESE SU CONTRASEÑA: "))
            print("****************************************************************")
            cursor.execute("SELECT USUARIOS,PASSWORD FROM USUARIOS WHERE idtest=1 ")
            USUARIOS = cursor.fetchall()
            for i in USUARIOS:

                if(i[1]==contraseña and i[0]== usuario):
                   cont=1;
                else:
                    cont=0;
                if(cont==1):
                    while ('true'):
                        print("----------------------------------------------------------------")
                        print('BIENVENIDO ADMINISTRADOR')
                        print('1. INGRESAR UN NUEVO USUARIO ')
                        print('2. ELIMINAR UN USUARIO ')
                        print('3. SALIR')
                        opcion=int(input("INTRODUZCA LA OPCION QUE DESEA: "))
                        if(opcion==1):
                            print("REGISTRO")
                            nombre=str(input("INGRESE SU NOMBRE DE USUARIO: "))
                            contraseña=str(input("INGRESE SU CONTRASEÑA: "))

                            sql_insert_query = """ INSERT INTO USUARIOS(USUARIOS,PASSWORD) VALUES (%s,%s)"""
                            record_to_insert = (nombre,contraseña)
                            cursor.execute(sql_insert_query, record_to_insert)
                            count = cursor.rowcount
                            conn.commit()
                            print()
                        elif (opcion == 2):
                            nombre=str(input("INGRESE EL NOMBRE DEL USUARIO QUE DESEA ELIMINAR: "))
                            sql_delete_query = "DELETE FROM USUARIOS WHERE USUARIOS= %s;"
                            cursor.execute(sql_delete_query,(nombre, ))
                            conn.commit()
                            print("ELIMINANDO...................")
                        elif(opcion==3):
                            print("Gracias por utilizar nuestro sistema")
                            cont=2;
                            opcion=3;
                            break

                        else:
                            print("INGRESE UNA DE LAS OPCIONES")
                elif(cont ==0):
                    for i in USUARIOS:
                        j=i;
                    for k in range(0, len(j)):
                        cursor.execute("SELECT USUARIOS,PASSWORD FROM USUARIOS WHERE idtest>1")
                        USUARIOS = cursor.fetchall()
                        for i in USUARIOS:
                            if(i[k]==usuario and i[k+1]==contraseña):
                                condicion=0
                                print("-----------BIENVENIDO "+usuario +"---------------------")
                                print("------------------------------")
                                print("| CLASES   | 1ra | 2da | 3ra |")
                                print("------------------------------")
                                print("|COMIDA    | 50  |  40 |  25 |")
                                print("|BEBIDA    | 35  | 25  | 10  |")
                                print("|PELICULA  | 70  | 55  | 25  |")
                                print("------------------------------")
                                conteo = int(input("CUANTOS BOLETOS VA A COMPRAR: "))
                                for i in range(1, conteo + 1):
                                    clase = int(input("INGRESE LA CLASE QUE DESEA EL BOLETO: "))
                                    cnt = int(input("INGRESE LA CANTIDAD DE SERVICIOS QUE DESEA: "))
                                    contador = cnt + contador
                                    servicio = []
                                    for i in range(1, cnt + 1):
                                        ser = str(input(" INGRESE EL SERVICIO DESEADO "))
                                        servicio.append(ser)
                                    ser1 = 0
                                    ser2 = 0
                                    ser3 = 0
                                    if (clase == 1):
                                        for i in range(0, cnt):
                                            if (servicio[i] == 'bebida'):
                                                ser1 = 35 + ser1
                                                m = 1
                                            elif (servicio[i] == 'comida'):
                                                ser2 = 50 + ser2
                                                n = 1
                                            elif (servicio[i] == 'pelicula'):
                                                ser3 = 70 + ser3
                                                o = 1
                                        total1 = ser1 + ser2 + ser3
                                    elif (clase == 2):
                                        for i in range(0, cnt):
                                            if (servicio[i] == 'bebida'):
                                                ser1 = 25 + ser1
                                            elif (servicio[i] == 'comida'):
                                                ser2 = 40 + ser2
                                            elif (servicio[i] == 'pelicula'):
                                                ser3 = 55 + ser3
                                        total2 = ser1 + ser2 + ser3
                                    elif (clase == 3):
                                        for i in range(0, cnt):
                                            if (servicio[i] == 'bebida'):
                                                ser1 = 10 + ser1
                                            elif (servicio[i] == 'comida'):
                                                ser2 = 25 + ser2
                                            elif (servicio[i] == 'pelicula'):
                                                ser3 = 25 + ser3
                                        total3 = ser1 + ser2 + ser3
                                    subtotal = total1 + total2 + total3
                                if (contador > 10 and m == 0) or (contador > 10 and n == 0) or (contador > 10 and o == 0):
                                    subdesc = subtotal - (subtotal * 0.1)
                                    DES = (subtotal * 0.1)
                                    sql_insert_query = """ INSERT INTO VUELOS(USUARIO,SUBTOTAL,DESCUENTO,DESCUENTO1,TOTAL) VALUES (%s,%s,%s,%s,%s)"""
                                    record_to_insert = (usuario,subtotal, '10%', DES, subdesc)
                                    cursor.execute(sql_insert_query, record_to_insert)
                                    count = cursor.rowcount
                                    conn.commit()
                                    print()
                                    print("El subtotal es: ", subtotal)
                                    print("Se realizo un descuento es del 10%")
                                    print("El descuento es de ", (subtotal * 0.1))
                                    print("El total es: ", subdesc)
                                elif (m == 1 and n == 1 and o == 1 and contador < 10):
                                    subdesc = subtotal - (subtotal * 0.05)
                                    DES = (subtotal * 0.05)
                                    sql_insert_query = """ INSERT INTO VUELOS(USUARIO,SUBTOTAL,DESCUENTO,DESCUENTO1,TOTAL) VALUES (%s,%s,%s,%s,%s)"""
                                    record_to_insert = (usuario,subtotal, '5%', DES, subdesc)
                                    cursor.execute(sql_insert_query, record_to_insert)
                                    count = cursor.rowcount
                                    conn.commit()
                                    print()
                                    print("El subtotal es: ", subtotal)
                                    print("Se realizo un descuento del 5%")
                                    print("El Descuento es de", (subtotal * 0.05))
                                    print("El total es: ", subdesc)
                                elif (m == 1 and n == 1 and o == 1 and contador > 10):
                                    subdesc = subtotal - (subtotal * 0.15)
                                    DES = (subtotal * 0.15)
                                    sql_insert_query = """ INSERT INTO VUELOS(USUARIO,SUBTOTAL,DESCUENTO,DESCUENTO1,TOTAL) VALUES (%s,%s,%s,%s,%s)"""
                                    record_to_insert = (usuario,subtotal, '15%', DES, subdesc)
                                    cursor.execute(sql_insert_query, record_to_insert)
                                    count = cursor.rowcount
                                    conn.commit()
                                    print()
                                    print("El subtotal es: ", subtotal)
                                    print("Se realizo un descuento del 15%")
                                    print("El Descuento es de", (subtotal * 0.15))
                                    print("El total es: ", subdesc)
                                else:
                                    sql_insert_query = """ INSERT INTO VUELOS(USUARIO,SUBTOTAL,DESCUENTO,DESCUENTO1,TOTAL) VALUES (%s,%s,%s,%s,%s)"""
                                    record_to_insert = (usuario, subtotal, 'SIN DESCUENTO', 0, subtotal)
                                    cursor.execute(sql_insert_query, record_to_insert)
                                    count = cursor.rowcount
                                    conn.commit()
                                    print()
                                    print("El subtotal es: ", subtotal)
                                    print("No hay descuento")
                                    print("El total es: ", subtotal)
                    if(condicion !=0):
                        print("USUARIO O CONTRASEÑA INVALIDA, POR FAVOR INTENTELO DE NUEVO")
        elif opcion ==2:
            print("----------------------MOSTRANDO HISTORIA------------------------")
            cursor.execute("SELECT USUARIO,SUBTOTAL, DESCUENTO, DESCUENTO1 TOTAL FROM VUELOS")
            VUELOS = cursor.fetchall()
            for i in VUELOS:
                print(i)
        elif opcion ==3:
            print("Gracias por utilizar nuestro sistema")
            conn.close()
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except:
        print("Error revisar los valores ingresados")