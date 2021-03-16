pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar los valores")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
  
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca el primer valor: ");
            V2 = input("Introduzca el segundo valor: ");
            disp('');
            if V1<V2
                n=V2;
                disp('Mostrando Conteo Descendente');
                fprintf(archivo,'Mostrando Conteo Descendente');
           
                for i=V1:V2
                    disp(n)
                    fprintf(archivo,'%i \n', n);
                    N=pq_exec_params(conn,"insert into PRO4 values($1);",{n});
                    n=n-1;
                endfor 
                fclose(archivo);         
            elseif V2<V1
                n=V1;
                disp('Mostrando Conteo Descendente')
                fprintf(archivo,'Mostrando Conteo Descendente');
                disp('');
                for i=V2 :V1
                    disp(n)
                    fprintf(archivo,'%i \n', n);
                    N=pq_exec_params(conn,"insert into PRO4 values($1);",{n});
                    n=n-1;
                endfor
                fclose(archivo);
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