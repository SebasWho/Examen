import os
Resultado=float()
opcion=str("")

while opcion!= "z":


    print ("Bienvenidos que Operacion Desea Realizar")
    print ("(s)  Suma")
    print ("(r)  Resta")
    print ("(m)  Multiplicación")
    print ("(d)  División")
    print ("(z)  Salir del Menu")

    try:
        opcion = input("Ingrese la letra que corresponde a la operacion que desea realizar: " )
        if opcion is "s":
            print("La operacion seleccionada fue suma")
            print("Ingrese el primer número")
            Dato_1=float(input())
            print("Ingrese el segundo número")
            Dato_2=float(input())
            Resultado= Dato_1+Dato_2
            print("El resultado de la sumatoria es: ", Resultado)

        elif opcion is "r":
            print("La operacion seleccionada fue resta")
            print("Ingrese el primer número")
            Dato_1=float(input())
            print("Ingrese el segundo número")
            Dato_2=float(input())
            Resultado= Dato_1-Dato_2
            print("El resultado de la resta es: ", Resultado)
        elif opcion is "m":
            print("La operacion seleccionada fue multiplicación")
            print("Ingrese el primer número")
            Dato_1=float(input())
            print("Ingrese el segundo número")
            Dato_2=float(input())
            Resultado= Dato_1*Dato_2
            print("El resultado de la multiplicación es: ", Resultado)
        elif opcion is "d":
            print("La operacion seleccionada fue división")
            print("Ingrese el primer número")
            Dato_1=float(input())
            print("Ingrese el segundo número")
            Dato_2=float(input())
            if Dato_2 != 0:
                Resultado= Dato_1/Dato_2
                print("El resultado de la división es: ", Resultado)
            elif Dato_2 == 0:
                print("No se puede realizar una división entre cero")
        elif opcion is "z":
            print("Gracias por utilizar nuestro sistema")
            clear=lambda:os.system("cls")
            clear()
        else:
            print("La opcion ingresada no es valida, vuelva a intentar")
    except :
         print ("Error operacion invalida")
