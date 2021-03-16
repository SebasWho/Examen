pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar Notas")
    disp("2. Mostrar el historial")
    disp("3. Salir")
    archivo=fopen('Salida.txt','a');
    cont=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca la primera nota: ");
            V2 = input("Introduzca la segunda nota: ");
            V3 = input("Introduzca la tercaera nota: ");
            Promedio=(V1+V2+V3)/3;
            printf('El promedio es: %i \n', Promedio)
            if Promedio>=60
                printf('*********APROBADO********* \n')
                fprintf(archivo,'El promedio es de: %i \n', Promedio);
                fprintf(archivo,'*********APROBADO********* \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO11 values($1,$2,$3,$4,$5);",{,V1,V2,V3,Promedio,'APROBADO'});
            elseif Promedio<60
                printf('*****REPROBADO**** \n')
                fprintf(archivo,'El promedio es de: %i \n', Promedio);
                fprintf(archivo,'*********REPROBADO********* \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO11 values($1,$2,$3,$4,$5);",{,V1,V2,V3,Promedio,'REPROBADO'});
            endif
         case{2}
            disp('Mostrando Historial')
            N=pq_exec_params(conn,'select * from PRO11;') 
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