
while (true)
    print ("Bienvenidos que Operacion Desea Realizar")
    print ("(s)  Suma")
    print ("(r)  Resta")
    print ("(m)  Multiplicación")
    print ("(d)  División")
    print ("(z)  Salir del Menu")
    try
    opcion=input("Ingrese la letra que corresponde a la operacion que desea realizar: ","s");
    switch opcion
      case{'s'}
            disp('La opcion seleccionada fue suma');
            Dato_1=input('Ingrese el primer numero: ');
            Dato_2=input('Ingrese el segundo numero: ');
            disp('El resultado de la sumatoria es: ');
            disp(Dato_1+Dato_2);
      case{'r'}
            disp('La opcion seleccionada fue resta');
            Dato_1=input('Ingrese el primer numero: ');
            Dato_2=input('Ingrese el segundo numero: ');
            disp('El resultado de la resta es: ');
            disp(Dato_1-Dato_2);
      case{'m'}
            disp('La opcion seleccionada fue multiplicación');
            Dato_1=input('Ingrese el primer numero: ');
            Dato_2=input('Ingrese el segundo numero: ');
            disp('El resultado de la multiplicación es: ');
            disp(Dato_1*Dato_2);
      case{'d'}
            disp('La opcion seleccionada fue suma');
            Dato_1=input('Ingrese el primer numero: ');
            Dato_2=input('Ingrese el segundo numero: ');
            if(Dato_2!=0)
              disp('El resultado de la sumatoria es: ');
              disp(Dato_1+Dato_2);
            else if Dato_2==0
              disp('No se puede realizar la división entre cero');
            endif
       case{'z'}
            disp('Gracias por utilizar nuestro sistema')
            break;
     otherwise
       disp('La opcion no se encuentra en el menu, intentelo de nuevo')
    endswitch
  catch
    disp('Error el valor ingresado no es numerico')  
  end
endwhile