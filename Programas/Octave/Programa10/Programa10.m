pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Ingresar lado para la comparacion")
    disp("2. Mostrar el historial")
    disp("3. Salir")
    archivo=fopen('Salida.txt','a');
    cont=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
            V1 = input("Introduzca el primer lado del triangulo: ");
            V2 = input("Introduzca el segundo lado del triangulo: ");
            V3 = input("Introduzca el tercer lado del triangulo: ");
            if V1==V2 && V2==V3
                printf('Es un triangulo Equilatero \n');
                fprintf(archivo,'Es un triangulo Equilatero \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO10 values($1,$2,$3,$4);",{V1,V2,V3,'Equilatero'});
            elseif V1!=V2 && V2!=V3 && V1!=V3
                printf('Es un triangulo Escaleno \n')
                fprintf(archivo,'Es un triangulo Escaleno \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO10 values($1,$2,$3,$4);",{V1,V2,V3,'Escaleno'});
            elseif (V1!=V2 && V1==V3)||(V1==V2 && V1!=V3)||(V2==V3 && V2!=V1) 
                printf('Es un triangulo Isosceles \n')
                fprintf(archivo,'Es un triangulo Isosceles \n');
                fclose(archivo); 
                N=pq_exec_params(conn,"insert into PRO10 values($1,$2,$3,$4);",{V1,V2,V3,'Isosceles'});
             endif
         case{2}
            disp('Mostrando Historial')
            N=pq_exec_params(conn,'select * from PRO10;') 
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