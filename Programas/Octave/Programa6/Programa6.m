pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar Palabra")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
    a=0;
    e=0;
    j=0;
    o=0;
    u=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca la palabra: ","s");
            disp('');     
            n=0;      
                for i=1:length(V1)
                    if V1(i)=='a' 
                      a=a+1;
                    elseif V1(i)=='e'
                      e=e+1;
                    elseif V1(i)=='i'
                      j=j+1;
                    elseif V1(i)=='o'
                      o=o+1;
                    elseif V1(i)=='u'
                      u=u+1;
                    endif
                  endfor  
                disp('La palabra tiene el siguiente numero de vocales')
                printf('A= %i  E= %i  I= %i  O= %i  U= %i \n',a,e,j,o,u)
                fprintf(archivo,'A= %i  E= %i  I= %i  O= %i  U= %i \n',a,e,j,o,u);
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO6 values($1,$2,$3,$4,$5);",{a,e,j,o,u});
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