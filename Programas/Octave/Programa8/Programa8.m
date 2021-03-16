pkg load database
conn=pq_connect(setdbopts('dbname','Tareas_Oc','host','localhost','port','5432','user','postgres','password','sebastian'));
while(true)
    disp ('-----------------------------------------------------------------')
    disp("Bienvenidos al sistema")
    disp("1. Calcular impares de 1 a 100")
    disp("2. Salir del programa")
    archivo=fopen('Salida.txt','a');
    cont=0;
   try        
        opcion=input("Indique que opcion desea realizar: ");
        switch opcion
          case{1}
          printf('Calculando los numeros impares......')
          fprintf(archivo,'Calculando los numeros impares......');
          for i=1 :100
          if mod(i,2)!= 0
            disp(i)
              fprintf(archivo,'%i \n',i);
              N=pq_exec_params(conn,"insert into PRO8 values($1);",{i});
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