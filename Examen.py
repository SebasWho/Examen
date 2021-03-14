import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Examen",
    user="postgres",
    password="sebastian"
)
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS P1")
cursor.execute("DROP TABLE IF EXISTS P2")
cursor.execute("DROP TABLE IF EXISTS P3")
cursor.execute("DROP TABLE IF EXISTS P4")
cursor.execute("DROP TABLE IF EXISTS P5")
sql1 = """CREATE TABLE P1(
     Altura_Mujeres float,
     Peso_Mujeres float,
     Altura_Hombres float,
     Peso_Hombres float
     )"""
sql2 = """CREATE TABLE P2(
     id int,
     Resultado_Diferencia int
     )"""
sql3 = """CREATE TABLE P3(
     id int,
     PRIMO_MAS_GRANDE integer
     )"""
sql4 = """CREATE TABLE P4(
     id int,
     Fibonacci integer[]
     )"""
sql5 = """CREATE TABLE P5(
     area_latera float,
     area_base float,
     area_total float,
     volumen float
     )"""

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
conn.commit()
id = 0
while ('true'):
    print('-----------------------------------')
    print('1. Estadistica de una Población')
    print('2. Calcular la diferencia entre la suma de cuadrados y el cuadrado de la suma')
    print('3. Numero mas grande de los primos')
    print('4. Calcular Fibonacci')
    print('5. Calculando las caracteristicas de un cono')
    print('6. Salir del Programa')
    archivo = open('201800690.txt', 'a')
    total1=0
    sum1 = 0
    sum2=0
    total2=0
    total3 = 0
    total4 = 0
    promedio=0
    contg=0
    conth = 0
    res=0
    i=0
    try:
        opcion = int(input('Que opcion desea escoger: '))
        if (opcion == 1):
            print('A escogido estadisticas de una población')
            reg = int(input('¿Cuantos regsitros ingresara?: '))
            while(i<reg):
                g = str(input('Introduzca el genero de la persona: '))
                if (g=='f'):
                    contg=contg+1
                    hf= float(input('Introduzca la altura de la persona: '))
                    pf= float(input('Introduzca el peso de la persona: '))
                    total1=total1+hf
                    total2=total2+pf
                elif(g=='m'):
                    conth=conth+1
                    hh = float(input('Introduzca la altura de la persona: '))
                    ph= float(input('Introduzca el peso de la persona: '))
                    total3 = total3 + hh
                    total4 = total4 + ph
                else:
                    print('Ingresar un genero')
                i=i+1

            prohf = total1 / contg
            propf = total2 / contg
            prohh = total3 / conth
            proph = total4 / conth
            print('Promedio de altura masculino')
            print(prohh)
            print('Promedio de peso masculino')
            print(proph)
            print('Promedio de altura femenino')
            print(prohf)
            print('Promedio de peso femenino')
            print(propf)
            archivo.write('*******PRIMER PROGRAMA********'+'\n')
            archivo.write('Promedio de altura masculino '+str(prohh)+'\n')
            archivo.write('Promedio de peso masculino ' + str(proph)+'\n')
            archivo.write('Promedio de altura femenino ' + str(prohf)+'\n')
            archivo.write('Promedio de peso femenino ' + str(propf)+'\n')
            archivo.close()
            sql_insert_query = """ INSERT INTO P1(Altura_Mujeres, Peso_Mujeres, Altura_Hombres, Peso_Hombres) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (prohf, propf,prohh,proph)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif (opcion == 2):
            j=0
            id=0
            id=id+1;
            print('A escogido la diferencia')
            for i in range(1,101):
                sum1=sum1+(i**2)
                sum2=sum2+i
            sum22=sum2**2
            res=sum22-sum1
            print('El resultado de la diferencia es: ', res)
            archivo.write('*******SEGUNDO PROGRAMA********' + '\n')
            archivo.write('El resultado de la diferencia es: '+str(res) +'\n')
            archivo.close()
            sql_insert_query = """ INSERT INTO P2(id,Resultado_Diferencia) VALUES (%s,%s)"""
            record_to_insert = (id,res)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif (opcion == 3):
            j=0
            id=0
            k=[]
            l=[]
            x=0
            id=id+1;
            cont1=0
            numero=1
            print('A escogido encontrar el numero mas grande de los primos de un numero')
            o=int(input('ingrese el valor deseado: '))
            for i in range(1,o+1):
                if o%i==0:
                    cont1=cont1+1
                    l.append(i)
            for g in range(1,cont1):
                x=0
                for numero in range(1,l[g]+1):
                    if l[g]%numero==0:
                        x=x+1
                if(x==2):
                    j=j+1
                    k.append(numero)
            print('EL valor mas alto primo es: ', k[j-1], end=' '+'\n')
            archivo.write('*******TERCER PROGRAMA********' + '\n')
            archivo.write('EL valor mas alto primo es: '+ str(k[j-1])+'\n')
            archivo.close()
            sql_insert_query = """ INSERT INTO P3(id,PRIMO_MAS_GRANDE) VALUES (%s,%s)"""
            record_to_insert = (id, k[j-1])
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif(opcion==4):
            vec= []
            id=0
            id=id+1
            V = int(input("Ingrese el valor n: "))
            def fib(valor):
                d1=0
                d2 =1
                for i in range(valor):
                    vec.append(d1)
                    d3=d1+d2
                    d1= d2
                    d2=d3
            fib(V)
            print("La sucession de fibonacci hasta el numero: ", V, " es: ", vec)
            archivo.write('*******CUARTO PROGRAMA********' + '\n')
            archivo.write("La sucession de fibonacci hasta el numero: "+ str(V)+ " es: "+ str(vec)+ '\n')
            archivo.close()
            sql_insert_query = """ INSERT INTO P4(id,Fibonacci) VALUES (%s,%s)"""
            record_to_insert = (id,vec)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif (opcion == 5):
            r=float(input('Ingrese el radio: '))
            g = float(input('Ingrese la generatriz: '))
            h = float(input('Ingrese la altura: '))
            arealateral=3.1416*r*g
            areabase=3.1416*(r**2)
            areatotal=arealateral+areabase
            volumen=(1/3)*(3.1416)*(r**2)*h
            print('El area lateral es: ',arealateral)
            print('El area de la base es: ', areabase)
            print('El area total es: ', areatotal)
            print('El volumen del cono es: ', volumen)
            archivo.write('*******QUINTO PROGRAMA********' + '\n')
            archivo.write('El area lateral es: '+ str(arealateral)+ '\n')
            archivo.write('El area de la base es: '+ str(areabase) + '\n')
            archivo.write('El area total es: '+ str(areatotal) + '\n')
            archivo.write('El volumen del cono es: '+ str(volumen)+ '\n')
            archivo.close()
            sql_insert_query = """ INSERT INTO P5(area_latera,area_base,area_total,volumen) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (arealateral,areabase,areatotal,volumen)
            cursor.execute(sql_insert_query, record_to_insert)
            count = cursor.rowcount
            conn.commit()
            print()
        elif (opcion == 6):
            print('Gracias por usar nuestro sistema')
            conn.close()
            archivo.close()
            break

        else:
            print('No se ha ingresado ninguna de las opciones')
    except:
        print('Se ha producido un error revisar los valores ingresados')