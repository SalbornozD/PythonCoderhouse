from django.shortcuts import render, redirect
from blog_manager.models import Noticia, Decreto
from django.contrib.auth import authenticate, login, logout

def index(request):
    data = {}
    
    # Si el usuario está autenticado, mostramos el botón de cerrar sesión
    data["is_authenticated"] = request.user.is_authenticated

    # Procesar inicio de sesión si los datos están en POST
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir a la misma página después del inicio de sesión
        else:
            data['login_error'] = 'Nombre de usuario o contraseña incorrectos'
    
    # Obtener todas las noticias ordenadas por fecha de publicación (recientes primero)
    noticias = Noticia.objects.all().order_by('-publication_date')
    
    # Separar noticias con y sin imágenes
    data["noticias_con_imagenes"] = noticias.filter(images__isnull=False).distinct()
    data["noticias_sin_imagenes"] = noticias.exclude(images__isnull=False)
    
    # titulares: noticias con imágenes más recientes
    data["titulares"] = data["noticias_con_imagenes"][:3]

    # Actualizar la lista de noticias para que no se repitan.
    data["noticias_con_imagenes"] = data["noticias_con_imagenes"][3:]
    
    # 4 decretos más recientes
    data["decretos"] = Decreto.objects.all().order_by('-id')[:4]
    
    return render(request, 'main/index.html', data)
