from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Member

#Defini mi pagina principal donde se registran cada uno de los trabajadores como index, le adiciona el @login_required para que no se pueda ingresar desde fuera solo con el url.  Con mem traigo todos los datos de la clase Member.
@login_required
def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

# Aqui cree la funcion add (adicionar o agregar) la cual me lleva al formulario para agregar nuevos trabajadores, tambien agregue el @login_required para que no se pueda ingresar desde fuera solo con la url.
@login_required
def add(request):
    return render(request, 'add.html')

# Aqui cree una nueva instancia del modelo member, guardo la nueva instancia en la base de datos y me redirije de nuevo a mi index, tambien agregue el @login_required para que no se pueda ingresar desde fuera solo con la url.
@login_required
def addrec(request):
    x = request.POST['Nombre']
    y = request.POST['Apellido']
    z = request.POST['Ciudad']
    mem=Member(nombre=x, apellido=y, ciudad=z)
    mem.save()
    return redirect("index")

# Aqui cree la funcion eliminar la cual me elimina al trabajador selecionado y  tambien agregue el @login_required para que no se pueda ingresar desde fuera solo con la url.
@login_required
def eliminar(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("index")

# Aqui cree la funcion de update (actualizar) con la cual puedo editar los datos de un trabajador ya creado, tambien agregue el @login_required para que no se pueda ingresar desde fuera solo con la url.
@login_required
def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

#aqui defini la funcion uprec (actualizar guardado) con la cual modifico los datos de los trabajadores con el id requerido y los guarda, tambien agregue el @login_required para que no se pueda ingresar desde fuera solo con la url.
@login_required
def uprec(request,id):
    x = request.POST['nombre']
    y = request.POST['apellido']
    z = request.POST['ciudad']
    mem=Member.objects.get(id=id)
    mem.nombre=x
    mem.apellido=y
    mem.ciudad=z
    mem.save()
    return redirect("index")


# Aqui defini el login (o iniciar sesion) si o si necesito estar logeado para poder ver los datos ya que estan protegidos, no se permite iniciar sino es un usuario registrado o valido.
def login_view(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            #Aqui mando el mensaje de error por si esque colocan mal los datos o colocan datos que no existen
            return render(request, 'login.html', {'error': 'Usuario o clave Incorrecta'})
    else:
        return render(request, 'login.html')

#Aqui tengo la funcion para cerrar sesion y me devuelve nuevamente a la ventana login
def logout_view(request):
    logout(request)
    return redirect('login')