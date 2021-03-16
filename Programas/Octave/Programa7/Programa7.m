pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Realizar la sumatoria")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
    resul=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca el valor deseado: ");
            disp('');     
    
               for i=1:V1
                    resul=resul+i;
                endfor
            printf('El resultado de la sumatoria hasta el numero %i es: %i \n',V1,resul)
            fprintf(archivo,'El resultado de la sumatoria hasta el numero %i es: %i \n',V1,resul);
            fclose(archivo); 
            N=pq_exec_params(conn,"insert into PRO7 values($1,$2);",{resul,V1});
          case{2}
            disp("Gracias por utilizar nuestro sistema")
            break
        otherwise
            disp('No se ingreso ninguna de las opciones vuelva a intentarlo')
        endswitch
    catch
      disp('Error los valores ingresados no son permitidos')
   
   end
    
endwhile