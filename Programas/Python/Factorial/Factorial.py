while 'true':
    archivo = open('Tarea.txt', 'a')
    resultado = 1
    i = 1
    print('----------------------------------------------------------------------------------')
    try:
        print("Bienvenidos al sistema")
        print("1. Calcular factorial")
        print("2. Salir")
        opcion=int(input("Indique que opcion desea realizar: "))

        if opcion == 1:
            print("Cual es el valor del cual desea el factorial ")
            fac=int(input())
            if fac<0:
                print("Error, no se puede calcular el factorial de un número negativo")
            else:
                if fac==0:
                    resultado=1
                    archivo.write('El factorial de '+ str(fac)+' es'+str(resultado) + '\n')
                    archivo.close()
                    print('El factorial de ', fac,' es',resultado)
                elif fac!=0:
                    for i in range(1,fac+1):
                        resultado=resultado*i
                    archivo.write('El factorial de '+ str(fac)+' es'+str(resultado)+'\n')
                    archivo.close()
                    print('El factorial de ',fac,'es',resultado)
        elif opcion ==2:
            print("Gracias por utilizar nuestro sistema")
            break
        else:
            print('No se ingreso ninguna de las opciones vuelva a intentarlo')
    except :
        print('Se ha producido un error revisar los datos ingresados')