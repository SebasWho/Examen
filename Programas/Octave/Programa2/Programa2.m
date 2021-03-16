pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar rangos")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
    n=0;
    
    try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            li = input("Introduzca el rango inferior: ");
            lf = input("Intruduzca el limite superior: ");
            i=li;
            if lf<=li
                disp("Error el limite superior no puede ser menor que el inferior")
            else
                disp("Mostrando el conteo");
                for n=0:round((lf-li)/2)
                    disp(i);
                    fprintf(archivo,'Mostrando conteo: %i  \n', i);
                    N=pq_exec_params(conn,"insert into PRO2 values($1);",{i});
                    i=i+2;
                endfor
                fclose(archivo); 
                printf('\n');
             endif
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
