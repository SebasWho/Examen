while(true)
    disp ('-----------------------------------------------------------------')
    disp ('Bienvenidos a nuestro sistema');
    disp ('[1]   Calcular el Factorial');
    disp ('[2]   Salir ');
    archivo=fopen('Tarea.txt','a');
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
                if fact==0         
                  printf ('El factorial de %i es %i \n',fact,resultado);
                  fprintf(archivo,'El factorial de %i es %i \n',fact,resultado);
                  fclose(archivo);
                elseif fact!=0
                  for n=1:fact
                    resultado=resultado*n;
                  endfor
                printf ('El factorial de %i es %i \n',fact,resultado);
                fprintf(archivo,'El factorial de %i es %i \n',fact,resultado);
                fclose(archivo);
              endif
            endif
          endif
          case {2}
            disp('Gracias por utilizar nuestro sistema');
            
            break
          otherwise
            disp('No se ha escogido una de las opciones')
        endswitch
    catch
      disp('Error los valores ingresados no son permitidos')
    end
    
endwhile
