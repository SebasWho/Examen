from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout 
from django.shortcuts import render,redirect
from users.models import regis,boletos

total1,total2,total3,subtotal,total,desc,contador,descuento=0,0,0,0,0,0,0,""
i=0
username,iden=" ",0

def logon(request):
    global total1,total2,total3,subtotal,total,contador,descuento,desc,i,username
    total1,total2,total3,subtotal,total,desc,contador,descuento,i=0,0,0,0,0,0,0,"",0
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        userSession=authenticate(request, username=username, password=password)
        if userSession:
            login(request,  userSession)
            return redirect("homepage")
        else:
            return render(request, 'login.html', {'error' : "Contraseña o usuario invalido"})    
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("logon")
def CITAS(request):
    return render(request,"Citas.html")
    
def registro(request):
    context={}
    if request.method=='POST':
        estado=False
        registro=regis()
        registro.nombre=request.POST['nombre']
        registro.edad=request.POST['edad']
        registro.peso=request.POST['peso']
        registro.altura=request.POST['altura']
        registro.fecha=request.POST['fecha']
        registro.hora=request.POST['hora']
        registro.save()
        estado=True
        context={
            "estado":estado
        }
    return render(request,"registro.html",context)
def buscar(request):
    if request.method=='POST':
        fecha=request.POST['fecha']
        pacientes=regis.objects.filter(fecha__contains=fecha)
        contexto={'paciente':pacientes}
        return render(request,"buscar.html",contexto)
    return render(request,"buscar.html")
def pacientes(request):

    pacientes=regis.objects.all()
    contexto={'paciente':pacientes}
    return render(request,"pacientes.html",contexto)

def borrar(request):
    contexto={}
    if(request.method=='POST'):
        boletos.objects.all().delete()
        contexto={'mensaje':'REGISTROS ELIMINADOS......'}
        return render(request,"vuelos.html",contexto)
    return render(request,"vuelos.html",contexto)

def bitacora(request):
    contexto={}
    try:
        if(request.method=='POST'):
            boton=request.POST['boton']
            if(boton=='1'):
                id1=request.POST.get('texto','15000')
                id2=int(id1)
                if(id2 !=0 and id2>0):
                    if(id2==15000):
                        return render(request,"eliminar.html")
                    else:
                        contexto={'mensaje':'REGISTRO ELIMINADO.....'}
                        boletos.objects.filter(id=id2).delete()
                        return render(request,"eliminar.html",contexto)
                elif(id2==0 or id2<0):
                    contexto={'error': 'ERROR: REVISAR DATOS INGRESADOS'}
                    return render(request,"eliminar.html",contexto)
            else:
                objetos=boletos.objects.all()
                contexto={'objeto': objetos}
                return render(request,"bitacora.html",contexto)
        return render(request,"eliminar.html",contexto) 
    except:
       contexto={'error' : 'ERROR: REVISAR DATOS INGRESADOS'}
    return render(request,"eliminar.html",contexto) 
       
def factura(request):
    global username
    usuario=username
    
    if request.method=='POST':
        subtotal=total1+total2+total3
        if(i==1 and contador<=10):
            desc=subtotal*0.05
            total=subtotal-desc
            descuento="5%"
        elif(i!=1 and contador>10):
            desc=subtotal*0.1
            total=subtotal-desc
            descuento="10%"
        elif(i==1 and contador>10):
            desc=subtotal*0.15
            total=subtotal-desc
            descuento="15%"
        else:
            total=subtotal
            descuento="0%"
            desc=0
        factura=boletos()
        factura.Usuario=usuario
        factura.subtotal=subtotal
        factura.Descuento=descuento
        factura.Valor=desc
        factura.total=total
        factura.save()
        iden=boletos.objects.latest('id','Usuario','subtotal','Descuento','Valor','total')
        contexto={'objeto':iden}
        return render(request,"factura.html",contexto)
    return render(request,"factura.html")
def VUELOS(request):
    try:
        global total1,total2,total3,subtotal,total,desc,descuento,contador
        global i
        contexto={}
        if request.method=='POST':
            clase1=0
            clase=request.POST.get('radio',False)
            comida=request.POST['COMIDA']
            bebida=request.POST['BEBIDA']
            pelicula=request.POST['PELICULA']
            clase1=int(clase)
            com1=int(comida)
            beb=int(bebida)
            pel=int(pelicula)
            contador=com1+beb+pel+contador
            if(clase1==0 or com1<0 or beb<0 or pel <0):
                contexto={'error' : "ERROR: Ingreso datos inválidos"}
            else:
                contexto={}
                if(clase1==1):
                    c1=50
                    b1=35
                    p1=70
                    total1=(c1*com1)+(b1*beb)+(p1*pel)+total1
                    if(com1!=0 and beb!= 0 and pel !=0):
                        i=1
                
                elif(clase1==2):
                
                    c2=40
                    b2=25
                    p2=55
                    total2=(c2*com1)+(b2*beb)+(p2*pel)+total2
                    
                elif(clase1==3):
                    c3=25
                    b3=10
                    p3=25
                    total3=(c3*com1)+(b3*beb)+(p3*pel)+total3
    except:
        contexto={'error' : "ERROR: Ingreso datos inválidos"}
    return render(request,"vuelos.html",contexto)

 