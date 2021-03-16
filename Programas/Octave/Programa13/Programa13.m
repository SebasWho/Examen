pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
     disp("Bienvenidos al sistema")
     disp("1. Ingresar año de nacimiento")
     disp("2. Mostrar historial")
     disp("3. Salir del programa")
    archivo=fopen('Salida.txt','a');
  try
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
         case{1}
            V1 = input("Introduzca su año de nacimiento: ");
            if mod(V1,4)==0 &&(mod(V1,100)!=0 || mod(V1,400)==0)
                printf('EL AÑO %i FUE UN AÑO BISIESTO \n',V1)
                fprintf(archivo,'EL AÑO %i FUE UN AÑO BISIESTO \n',V1);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO13 values($1,$2);",{V1,'BISIESTO'});
            else 
                printf('EL AÑO %i NO FUE UN AÑO BISIESTO \n',V1)
                fprintf(archivo,'EL AÑO %i NO FUE UN AÑO BISIESTO \n',V1);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO13 values($1,$2);",{V1,'NO BISIESTO'});
             endif
         case{2}
            disp('Mostrando Historial')
            N=pq_exec_params(conn,'select * from PRO13;') 
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