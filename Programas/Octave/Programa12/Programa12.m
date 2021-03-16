pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp ('Bienvenidos a nuestro sistema');
    disp ('[1]   Calcular el Factorial');
    disp ('[2]   Mostrar Historial ');
    disp ('[3]   Salir ');
    archivo=fopen('Salida.txt','a');
    resultado=1;
    
    
    try
      opcion = input("Ingrese la opcion que desea realizar: ");
        switch opcion
          case {1}
            disp('Su opcion es calcular el factorial')
            fact=input('Ingrese el número que desea calcular el factorial: ');
            decimal=round(fact);
            if((fact-decimal)!=0)
              disp("Error no se puede calcular el factorial de un numero decimal");
            else              
              if fact<0
                  disp('Error, no se puede calcular el factorial de un número negativo');
              else 
                if mod(fact,7)==0
                  for n=1:fact
                    resultado=resultado*n;
                  endfor
                printf ('El factorial de %i es %i \n',fact,resultado);
                fprintf(archivo,'El factorial de %i es %i \n',fact,resultado);
                fclose(archivo);
                N=pq_exec_params(conn,"insert into PRO12 values($1,$2);",{fact,resultado});
              endif
            endif
          endif
         case{2}
            disp('Mostrando Historial')
            N=pq_exec_params(conn,'select * from PRO12;') 
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