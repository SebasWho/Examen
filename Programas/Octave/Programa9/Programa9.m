pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Calcular area del Circulo")
    disp("2. Calcular area del Triangulo")
    disp("3. Calcular area del Cuadrado")
    disp("4. Calcular area del Rectangulo")
    disp("5. Mostrar historial")
    disp("6. Salir del programa")
    archivo=fopen('Salida.txt','a');
    cont=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
          printf('A escogido calcular el area de un circulo \n')
            V1 = input("Introduzca el radio: ");
            resul= pi*(V1^2);
            printf('El area del circulo es: %i \n', resul)
            fprintf(archivo,'El area del circulo es: %i \n', resul);
            fclose(archivo); 
            N=pq_exec_params(conn,"insert into PRO9 values($1,$2);",{'Circulo',resul});
          case{2}
            disp('A escogido calcular el area de un Triangulo')
            b = input("Introduzca la base: ");
            h= input('Introduzca la altura: ');
            resul = (b*h)/2;
            printf('El area del triangulo es: %i \n', resul);
            fprintf(archivo,'El area del Triangulo es: %i \n', resul);
            fclose(archivo); 
            N=pq_exec_params(conn,"insert into PRO9 values($1,$2);",{'Triangulo',resul});
          case{3}
            disp('A escogido calcular el area de un cuadrado')
            b = input("Introduzca la base: ");
            resul = b*b;
            printf('El area del cuadrado es: %i \n', resul)
            fprintf(archivo,'El area del cuadrado es: %i \n', resul);
            fclose(archivo); 
            N=pq_exec_params(conn,"insert into PRO9 values($1,$2);",{'Cuadrado',resul});
          case{4}
            disp('A escogido calcular el area de un rectangulo')
            b = input("Introduzca la base: ");
            L = input("Introduzca el lado: ");
            resul = b * L;
            printf('El area del rectangulo es: %i \n', resul)
            fprintf(archivo,'El area del cuadrado es: %i \n', resul);
            fclose(archivo); 
            N=pq_exec_params(conn,"insert into PRO9 values($1,$2);",{'Rectangulo',resul});
          case{5}
            disp('Mostrnado Historial')
            N=pq_exec_params(conn,'select * from PRO9;')
          case{6}
          disp("Gracias por utilizar nuestro sistema")
            break
        otherwise
            disp('No se ingreso ninguna de las opciones vuelva a intentarlo')
        endswitch
    catch
      disp('Error los valores ingresados no son permitidos')
   
   end
    
endwhile