pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
     disp("Bienvenidos al sistema")
     disp("1. Ingresar Datos del Automovil")
     disp("2. Mostrar historial")
     disp("3. Salir del programa")
    archivo=fopen('Salida.txt','a');
  try
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
         case{1}
            V1 = input("Ingrese el modelo del Automovil: ");
            V2 = input("Ingrese los kilometros que lleva recorrido: ");
            if V1<2007 && V2>20000
                printf('El Automovil Modelo %i debe renovarse \n', V1)
                fprintf(archivo,'El Automovil Modelo %i debe renovarse \n', V1);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO14 values($1,$2,$3);",{V1,V2,'RENOVARSE'});
            elseif  V1>=2007 && V1<=2013 && V2==20000
                printf('El automovil modelo %i debe recibir mantenimiento \n',V1)
                fprintf(archivo,'El automovil modelo %i debe recibir mantenimiento \n',V1);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO14 values($1,$2,$3);",{V1,V2,'MANTENIMIENTO'});
            elseif V1 >2013 && V2 < 10000
                printf('El automovil modelo %i esta en optimas condiciones \n',V1)
                fprintf(archivo,'El automovil modelo %i esta en optimas condiciones \n',V1);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO14 values($1,$2,$3);",{V1,V2,'OPTIMAS DE CONDICIONES'});
            else
                printf('MECANICO \n')
                fprintf(archivo,'MECANICO \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO14 values($1,$2,$3);",{V1,V2,'MECANICO'});
            endif
         case{2}
            disp('Mostrando Historial')
            N=pq_exec_params(conn,'select * from PRO14;') 
         case{3}
          disp("Gracias por utilizar nuestro sistema")
            break
        otherwise
            disp('No se ingreso ninguna de las opciones vuelva a intentarlo')
        endswitch
    catch
      disp('Error los valores ingresados no son permitidos')  
   end
endwhile