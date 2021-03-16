pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar Palabra")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
  
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca la palabra: ","s");
            disp('');     
            n=0;      
                for i=1:length(V1)
                    if V1(i)=='a'||V1(i)=='e' || V1(i)=='i' || V1(i)=='o'||V1(i)=='u'
                      n=n+1;
                    endif
                  endfor  
                printf('La palabra %s tiene %i vocales',V1,n)
                printf('\n')
                fprintf(archivo,'La palabra %s tiene %i vocales \n',V1,n);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO5 values($1);",{n});
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