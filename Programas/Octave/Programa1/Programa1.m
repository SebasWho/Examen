pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp ('Bienvenidos a nuestro sistema');
    disp ('[1]   Ingresar los valores a comparar');
    disp ('[2]   Salir ');
    
    archivo=fopen('Tarea.txt','a');
    resultado =1;
    try
        opcion=input("Ingrese la opcion que desea elegir: ");
        switch opcion
          case {1}
            V1 = input("Ingrese el primer numero: ");
            V2 = input("Ingrese el segundo numero : ");
            V3 = input("Ingrese el tercer numero: ");
            disp('Comparando valores');

            if V1>V2 && V1>V3 && V3!=V1 && V2!=V1 && V2!=V3
                resultado=V1+V2+V3; 
                printf ('El resultado de la sumatoria es: %i \n',resultado);
                fprintf(archivo,'El resultado de la sumatoria es: %i \n',resultado);
                fclose(archivo);
                N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{resultado,0,0,0,'SON DISTINTOS'});
            elseif V2>V1 && V2>V3 && V3!=V1 && V2!=V1 && V2!=V3
                resultado=V1*V2*V3; 
                printf ('El resultado de la multiplicación es: %i \n',resultado);
                fprintf(archivo,'El resultado de la multiplicación es: %i \n',resultado);
                fclose(archivo);
                N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,resultado,0,0,'SON DISTINTOS'});
             elseif V3>V1 && V3>V2 && V3!=V1 && V2!=V1 && V2!=V3
                A=strcat(num2str(V1),num2str(V2),num2str(V3));
                printf ('El resultado de la concatenación es: %i%i%i \n',V1,V2,V3);
                fprintf(archivo,'El resultado de la concatenación es: %i%i%i \n',V1,V2,V3);
                fclose(archivo);
                N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,0,A,0,'SON DISTINTOS'});
             elseif V1==V2 && V3!=V1
                  printf ('El Valor distinto es: %i \n',V3);
                  fprintf(archivo,'El Valor distinto es: %i \n',V3);
                  fclose(archivo);
                  N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,0,0,V3,'SON DISTINTOS'});
             elseif V2==V3 && V3!=V1
                  printf ('El Valor distinto es: %i \n',V1);
                  fprintf(archivo,'El Valor distinto es: %i \n',V1);
                  fclose(archivo);
                  N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,0,0,V1,'SON DISTINTOS'});
             elseif V1==V3 && V2!=V1
                  printf ('El Valor distinto es: %i \n',V2);
                  fprintf(archivo,'El Valor distinto es: %i \n',V2);
                  fclose(archivo);
                  N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,0,0,V2,'SON DISTINTOS'});
              elseif(V1==V3 && V2==V3)
                printf ('Los valores ingresados son: %i  %i  %i \n',V1,V2,V3);
                printf ('Son iguales');
                fprintf(archivo,'Los valores ingresados son: %i  %i  %i \n',V1,V2,V3);
                fprintf(archivo,'Son iguales');
                fclose(archivo);
                N=pq_exec_params(conn,"insert into PRO1 values($1,$2,$3,$4,$5);",{0,0,0,0,'SON IGUALES'});
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
