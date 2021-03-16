pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Obtener los Divisores")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
    Id=0;
    try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca el valor del cual desea calcular los divisores: ");
            disp("Calculando......");
            printf('Los divisores de %i son: \n',V1);
            fprintf(archivo,'Los divisores de %i son: \n',V1);
            disp('');
            for i=1:V1
                if mod(V1,i)==0
                    disp(i);
                    fprintf(archivo,'%i \n', i);
                    N=pq_exec_params(conn,"insert into PRO3 values($1);",{i});
                 endif
            endfor
            fclose(archivo);
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
