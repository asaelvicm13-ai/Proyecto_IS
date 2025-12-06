
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.db import connection
from .models import Usuario, Generos  # Asegúrate de importar ambos
import json
import random

@csrf_exempt
def guardar_usuario(request):
    """Vista para guardar usuario después de verificación de email"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extraer datos
            nombre = data.get('name')
            email = data.get('email')
            username = data.get('username')
            password = data.get('password')
            
            # Verificar si el email ya existe
            if Usuario.objects.filter(email=email).exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Ya existe una cuenta con ese email'
                })
            
            # OPCIÓN 1: Crear usuario solo con campos que existen
            try:
                nuevo_usuario = Usuario(
                    nombre=username,
                    email=email,
                    contrasena=make_password(password)  # Hashear la contraseña
                )
                nuevo_usuario.save()
                
                # Actualizar campos adicionales con SQL directo si es necesario
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE usuarios 
                        SET es_email_verificado = 1, es_admin = 0, apellido = ''
                        WHERE usuario_id = %s
                    """, [nuevo_usuario.usuario_id])
                
            except Exception as e:
                # OPCIÓN 2: Si falla, usar SQL directo completamente
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO usuarios (nombre, apellido, email, contrasena, es_email_verificado, es_admin)
                        VALUES (%s, %s, %s, %s, 1, 0)
                    """, [username, '', email, password])
                    
                    # Obtener el ID del usuario recién creado
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    usuario_id = cursor.fetchone()[0]
                    
                    nuevo_usuario = Usuario.objects.get(usuario_id=usuario_id)
            
            # Auto-login después del registro
            request.session['usuario_id'] = nuevo_usuario.usuario_id
            request.session['usuario_nombre'] = nuevo_usuario.nombre
            request.session['usuario_email'] = nuevo_usuario.email
            
            return JsonResponse({
                'success': True,
                'message': 'Usuario registrado exitosamente',
                'redirect_url': '/home/'
            })
            
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
            return JsonResponse({
                'success': False,
                'message': f'Error al registrar: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
def login_view(request):
    """Vista para el login de usuarios"""
    if request.method == 'POST':
        # Obtener los datos del formulario con los nombres correctos
        username_or_email = request.POST.get('userName') or request.POST.get('email')
        password = request.POST.get('passWord') or request.POST.get('password')
        
        print(f"Datos recibidos - Usuario: {username_or_email}, Password: {password}")
        print(f"Todos los datos POST: {request.POST}")
        
        # Validar que los campos no estén vacíos
        if not username_or_email or not password:
            messages.error(request, 'Por favor ingresa usuario/email y contraseña')
            return render(request, 'interfaz/LoginScreen.html')
        
        try:
            # Buscar usuario - primero verificar si es email
            if '@' in str(username_or_email):
                try:
                    usuario = Usuario.objects.get(email=username_or_email)
                except Usuario.DoesNotExist:
                    messages.error(request, 'No existe una cuenta con ese email')
                    return render(request, 'interfaz/LoginScreen.html')
            else:
                # Buscar por nombre
                try:
                    usuario = Usuario.objects.get(nombre=username_or_email)
                except Usuario.DoesNotExist:
                    messages.error(request, 'No existe una cuenta con ese nombre de usuario')
                    return render(request, 'interfaz/LoginScreen.html')
            
            print(f"✅ Usuario encontrado: ID={usuario.usuario_id}, Nombre={usuario.nombre}")
            print(f"📝 Contraseña en BD: '{usuario.contrasena}'")
            print(f"⌨️ Contraseña ingresada: '{password}'")
            
            # IMPORTANTE: Comparar contraseñas DIRECTAMENTE (sin hash en tu caso)
            if password == usuario.contrasena:
                print(f"✅ Contraseña correcta!")
                # Login exitoso
                request.session['usuario_id'] = usuario.usuario_id
                request.session['usuario_nombre'] = usuario.nombre
                request.session['usuario_email'] = usuario.email
                
                # Verificar si ya tiene géneros seleccionados
                if 'generos_favoritos' in request.session and len(request.session['generos_favoritos']) == 3:
                    return redirect('lista_reproduccion')
                else:
                    return redirect('home')
            else:
                print(f"❌ Contraseña incorrecta")
                messages.error(request, 'Contraseña incorrecta')
                
        except Usuario.DoesNotExist:
            messages.error(request, 'No existe una cuenta con esos datos')
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            messages.error(request, f'Error: {str(e)}')
        
        return render(request, 'interfaz/LoginScreen.html')
    
    return render(request, 'interfaz/LoginScreen.html')
def registro_view(request):
    """Vista para registro de nuevos usuarios"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validaciones
        if not all([nombre, apellido, email, password]):
            messages.error(request, 'Todos los campos son obligatorios')
            return render(request, 'interfaz/registro.html')
        
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'interfaz/registro.html')
        
        # Verificar si el email ya existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe una cuenta con ese email')
            return render(request, 'interfaz/registro.html')
        
        try:
            # Crear nuevo usuario
            nuevo_usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email,
                contrasena=password,  # En producción usar make_password(password)
                foto_perfil_path='/static/interfaz/imagenes/inicio/default-avatar.png'
            )
            nuevo_usuario.save()
            
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f'Error al crear la cuenta: {str(e)}')
            return render(request, 'interfaz/registro.html')
    
    return render(request, 'interfaz/registro.html')
def logout_view(request):
    """Vista para cerrar sesión"""
    request.session.flush()  # Limpiar toda la sesión
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('login')
def seleccionar_generos(request):
    """Modificar la vista existente para requerir login"""
    # Verificar si el usuario está logueado
    if 'usuario_id' not in request.session:
        messages.warning(request, 'Debes iniciar sesión primero')
        return redirect('login')
    
    
    # Rutas correctas según tu estructura
    imagenes_generos = {
        'Rock': 'interfaz/imagenes/generos/gen_vaca_rockera.png',
        'Pop': 'interfaz/imagenes/generos/gen_vaca_pop.png',
        'Jazz': 'interfaz/imagenes/generos/gen_vaca_jazz.png',
        'Hip-hop': 'interfaz/imagenes/generos/gen_vaca_hiphop.png',
        'Electronic': 'interfaz/imagenes/generos/gen_vaca_electronica.png',
        'Classical': 'interfaz/imagenes/generos/gen_vaca_clasica.png',
        'Reggae': 'interfaz/imagenes/generos/gen_vaca_reggaeton.png',
        'Metal': 'interfaz/imagenes/generos/gen_vaca_metal.png',
        'Country': 'interfaz/imagenes/generos/gen_vaca_alternativo.png',
        'R&B': 'interfaz/imagenes/generos/gen_vaca_rb.png',
    }
    
    try:
        from .models import Generos
        generos_db = Generos.objects.all()
        
        if generos_db.exists():
            generos = []
            for g in generos_db[:10]:
                imagen_path = imagenes_generos.get(g.nombre, 'interfaz/imagenes/generos/gen_vaca_alternativo.png')
                generos.append({
                    'nombre': g.nombre,
                    'valor': g.nombre,
                    'imagen': imagen_path,
                    'usar_static': True
                })
        else:
            generos = []
            for nombre, imagen_path in imagenes_generos.items():
                generos.append({
                    'nombre': nombre,
                    'valor': nombre,
                    'imagen': imagen_path,
                    'usar_static': True
                })
    except Exception as e:
        print(f"Error: {e}")
        generos = []
        for nombre, imagen_path in imagenes_generos.items():
            generos.append({
                'nombre': nombre,
                'valor': nombre,
                'imagen': imagen_path,
                'usar_static': True
            })
    
    # DEBUG: Imprimir para verificar
    print(f"Géneros a mostrar: {len(generos)}")
    for g in generos:
        print(f"  - {g['nombre']}: {g['imagen']}")
    
    context = {
        'generos': generos
    }
    return render(request, 'interfaz/seleccionar_generos.html', context)
def guardar_generos(request):
    """Vista para procesar los géneros seleccionados"""
    if request.method == 'POST':
        # Verificar si es petición AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                generos_seleccionados = data.get('generos', [])
            except:
                generos_seleccionados = request.POST.getlist('generos')
        else:
            generos_seleccionados = request.POST.getlist('generos')
        
        # Validaciones
        if len(generos_seleccionados) != 3:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Debes seleccionar exactamente 3 géneros'})
            messages.error(request, 'Debes seleccionar exactamente 3 géneros')
            return redirect('home')
        
        # Guardar en sesión
        request.session['generos_favoritos'] = generos_seleccionados
        
        # Debug
        print(f"✅ Géneros seleccionados: {generos_seleccionados}")
        
        # Respuesta AJAX o redirección normal
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': 'Géneros guardados exitosamente',
                'generos': generos_seleccionados,
                'redirect_url': '/lista-reproduccion/'
            })
        
        return redirect('lista_reproduccion')
    
    return redirect('home')
def lista_reproduccion(request):
    """Vista para mostrar las canciones reales de la BD"""
    generos_seleccionados = request.session.get('generos_favoritos', [])
    
    if not generos_seleccionados or len(generos_seleccionados) != 3:
        messages.warning(request, 'Primero debes seleccionar 3 géneros musicales')
        return redirect('home')
    
    # Obtener ID del usuario logueado
    usuario_id = request.session.get('usuario_id')

    todas_las_canciones = []
    
    try:
        # Usar SQL directo para obtener las canciones
        with connection.cursor() as cursor:
            # Query para obtener canciones con sus relaciones, likes/dislikes
            query = """
                SELECT 
                    c.cancion_id,
                    c.titulo,
                    c.duracion,
                    c.ruta_archivo,
                    a.titulo as album,
                    a.imagen_portada_path,
                    ar.nombre as artista,
                    g.nombre as genero,
                    COALESCE(likes.total, 0) as likes,
                    COALESCE(dislikes.total, 0) as dislikes,
                    rc.tipo as reaccion_usuario,
                    COALESCE(ratings.avg_rating, 0) as promedio_rating,
                    COALESCE(ratings.total_ratings, 0) as total_ratings,
                    COALESCE(user_rating.valor, 0) as user_rating
                FROM canciones c
                LEFT JOIN albumes a ON c.album_id = a.album_id
                LEFT JOIN canciones_artistas ca ON c.cancion_id = ca.cancion_id 
                    AND ca.tipo_participacion = 'Principal'
                LEFT JOIN artistas ar ON ca.artista_id = ar.artista_id
                LEFT JOIN canciones_generos cg ON c.cancion_id = cg.cancion_id
                LEFT JOIN generos g ON cg.genero_id = g.genero_id
                LEFT JOIN (
                    SELECT cancion_id, COUNT(*) as total 
                    FROM reacciones_canciones 
                    WHERE tipo = 'like' 
                    GROUP BY cancion_id
                ) likes ON c.cancion_id = likes.cancion_id
                LEFT JOIN (
                    SELECT cancion_id, COUNT(*) as total 
                    FROM reacciones_canciones 
                    WHERE tipo = 'dislike' 
                    GROUP BY cancion_id
                ) dislikes ON c.cancion_id = dislikes.cancion_id
                LEFT JOIN reacciones_canciones rc ON c.cancion_id = rc.cancion_id 
                    AND rc.usuario_id = %s
                LEFT JOIN (
                    SELECT 
                        cancion_id, 
                        AVG(valor) as avg_rating,
                        COUNT(*) as total_ratings
                    FROM ratings_canciones 
                    GROUP BY cancion_id
                ) ratings ON c.cancion_id = ratings.cancion_id
                LEFT JOIN ratings_canciones user_rating ON c.cancion_id = user_rating.cancion_id 
                    AND user_rating.usuario_id = %s
                WHERE g.nombre IN (%s, %s, %s)
                ORDER BY RAND()
                LIMIT 30
            """
            # Parámetros: usuario_id para reacción personal, luego los 3 géneros
            params = [usuario_id, usuario_id] + generos_seleccionados
            
            print(f"🔍 Parámetros: {params}")
            print(f"📝 Géneros: {generos_seleccionados}")

            cursor.execute(query, params)
            canciones_db = cursor.fetchall()
            
            print(f"✅ Canciones encontradas: {len(canciones_db)}")
            
            # Convertir resultados a diccionarios
            for cancion in canciones_db:
                # Formatear duración
                duracion = str(cancion[2]) if cancion[2] else "0:00"
                if len(duracion) > 5:
                    duracion = duracion[3:8]  # Tomar solo MM:SS
                
                # Asegurar que la portada tenga URL válida
                portada = cancion[5] if cancion[5] else '/static/interfaz/imagenes/default_cover.png'
                # Si es una ruta relativa, convertirla a URL estática
                if portada.startswith('interfaz/imagenes/'):
                    portada = f'/static/{portada}'
                
                todas_las_canciones.append({
                    'id': cancion[0],
                    'titulo': cancion[1],
                    'duracion': duracion,
                    'ruta_archivo': cancion[3],
                    'album': cancion[4] if cancion[4] else 'Sin álbum',
                    'portada': portada,
                    'artista': cancion[6] if cancion[6] else 'Artista desconocido',
                    'genero': cancion[7] if cancion[7] else 'Sin género',
                    'likes': int(cancion[8]),
                    'dislikes': int(cancion[9]),
                    'reaccion_usuario': cancion[10],  # 'like', 'dislike' o None
                    'promedio_rating': float(cancion[11]),  # promedio de rating
                    'total_ratings': int(cancion[12]),  # total de calificaciones
                    'user_rating': int(cancion[13])  # rating del usuario actual (1-5)
                })
                
        print(f"✅ Se cargaron {len(todas_las_canciones)} canciones reales de la BD")
                
    except Exception as e:
        print(f"❌ Error al obtener canciones de la BD: {e}")
        import traceback
        traceback.print_exc()
        messages.error(request, 'Error al cargar las canciones. Por favor, intenta de nuevo.')
        # Si hay error, dejamos la lista vacía - NO agregamos canciones demo
    
    # Verificar si hay suficientes canciones
    if len(todas_las_canciones) == 0:
        messages.warning(request, 'No hay canciones disponibles en los géneros seleccionados')
        print("⚠️ No se encontraron canciones en los géneros:", generos_seleccionados)
    
    # Mezclar las canciones
    random.shuffle(todas_las_canciones)
    
    context = {
        'canciones': todas_las_canciones,
        'generos_seleccionados': generos_seleccionados,
        'total_canciones': len(todas_las_canciones)
    }
    
    return render(request, 'interfaz/lista_reproduccion.html', context)

@csrf_exempt
@csrf_exempt
def calificar_cancion(request):
    """Vista para calificar canciones con estrellas (1-5)"""
    if request.method == 'POST':
        try:
            # Verificar si hay sesión activa
            if 'usuario_id' not in request.session:
                return JsonResponse({
                    'success': False,
                    'message': 'Debes iniciar sesión para calificar canciones'
                })
            
            data = json.loads(request.body)
            cancion_id = data.get('cancion_id')
            rating_value = int(data.get('rating', 0))  # 0 = eliminar rating
            usuario_id = request.session['usuario_id']
            
            print(f"⭐ Usuario {usuario_id} calificando canción {cancion_id} con {rating_value} estrellas")
            
            # Validar valor del rating
            if rating_value < 0 or rating_value > 5:
                return JsonResponse({
                    'success': False,
                    'message': 'El rating debe estar entre 1 y 5'
                })
            
            with connection.cursor() as cursor:
                if rating_value == 0:
                    # Eliminar rating del usuario para esta canción
                    cursor.execute("""
                        DELETE FROM ratings_canciones 
                        WHERE usuario_id = %s AND cancion_id = %s
                    """, [usuario_id, cancion_id])
                    print(f"❌ Rating eliminado para canción {cancion_id}")
                    accion = 'eliminado'
                else:
                    # Verificar si ya existe un rating del usuario
                    cursor.execute("""
                        SELECT rating_id FROM ratings_canciones 
                        WHERE usuario_id = %s AND cancion_id = %s
                    """, [usuario_id, cancion_id])
                    
                    rating_existente = cursor.fetchone()
                    
                    if rating_existente:
                        # Actualizar rating existente
                        cursor.execute("""
                            UPDATE ratings_canciones 
                            SET valor = %s, fecha_rating = NOW()
                            WHERE usuario_id = %s AND cancion_id = %s
                        """, [rating_value, usuario_id, cancion_id])
                        print(f"🔄 Rating actualizado a {rating_value} para canción {cancion_id}")
                        accion = 'actualizado'
                    else:
                        # Insertar nuevo rating
                        cursor.execute("""
                            INSERT INTO ratings_canciones (usuario_id, cancion_id, valor)
                            VALUES (%s, %s, %s)
                        """, [usuario_id, cancion_id, rating_value])
                        print(f"✅ Nuevo rating {rating_value} agregado para canción {cancion_id}")
                        accion = 'agregado'
                
                # Obtener estadísticas actualizadas del rating
                cursor.execute("""
                    SELECT 
                        COUNT(*) as total_ratings,
                        AVG(valor) as promedio
                    FROM ratings_canciones
                    WHERE cancion_id = %s
                """, [cancion_id])
                
                estadisticas = cursor.fetchone()
                total_ratings = estadisticas[0] if estadisticas[0] else 0
                promedio = float(estadisticas[1]) if estadisticas[1] else 0.0
                
                # Si se eliminó el rating, obtener el nuevo rating del usuario (será 0)
                user_rating = rating_value if rating_value > 0 else 0
                
                print(f"📊 Estadísticas actualizadas: Promedio={promedio:.1f}, Total={total_ratings}")
                
                return JsonResponse({
                    'success': True,
                    'promedio': round(promedio, 1),
                    'total_ratings': total_ratings,
                    'user_rating': user_rating,
                    'accion': accion,
                    'message': f'Rating {accion} exitosamente'
                })
                
        except Exception as e:
            print(f"❌ Error al calificar canción: {e}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Método no permitido'
    })

def obtener_estadisticas_rating(request, cancion_id):
    """Obtener estadísticas detalladas del rating de una canción"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_ratings,
                    AVG(valor) as promedio,
                    MIN(valor) as min_rating,
                    MAX(valor) as max_rating,
                    COUNT(CASE WHEN valor = 5 THEN 1 END) as rating_5,
                    COUNT(CASE WHEN valor = 4 THEN 1 END) as rating_4,
                    COUNT(CASE WHEN valor = 3 THEN 1 END) as rating_3,
                    COUNT(CASE WHEN valor = 2 THEN 1 END) as rating_2,
                    COUNT(CASE WHEN valor = 1 THEN 1 END) as rating_1
                FROM ratings_canciones 
                WHERE cancion_id = %s
            """, [cancion_id])
            
            resultado = cursor.fetchone()
            
            return JsonResponse({
                'success': True,
                'total_ratings': resultado[0] or 0,
                'promedio': float(resultado[1]) if resultado[1] else 0.0,
                'min_rating': resultado[2] or 0,
                'max_rating': resultado[3] or 0,
                'distribucion': {
                    '5_estrellas': resultado[4] or 0,
                    '4_estrellas': resultado[5] or 0,
                    '3_estrellas': resultado[6] or 0,
                    '2_estrellas': resultado[7] or 0,
                    '1_estrella': resultado[8] or 0,
                }
            })
            
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })

@csrf_exempt
def buscar_canciones(request):
    """Vista para buscar canciones - BÚSQUEDA GLOBAL"""
    if request.method == 'GET':
        termino = request.GET.get('q', '').strip()
        usuario_id = request.session.get('usuario_id')
        print(f"🔍 Búsqueda: '{termino}'")
        
        if len(termino) < 2:
            return JsonResponse({
                'success': False,
                'message': 'Ingresa al menos 2 caracteres'
            })
        
        try:
            with connection.cursor() as cursor:
                query = """
                    SELECT DISTINCT
                        c.cancion_id,
                        c.titulo,
                        c.duracion,
                        c.ruta_archivo,
                        a.titulo as album,
                        a.imagen_portada_path,
                        ar.nombre as artista,
                        g.nombre as genero,
                        COALESCE(likes.total, 0) as likes,
                        COALESCE(dislikes.total, 0) as dislikes,
                        rc.tipo as reaccion_usuario
                    FROM canciones c
                    LEFT JOIN albumes a ON c.album_id = a.album_id
                    LEFT JOIN canciones_artistas ca ON c.cancion_id = ca.cancion_id 
                        AND ca.tipo_participacion = 'Principal'
                    LEFT JOIN artistas ar ON ca.artista_id = ar.artista_id
                    LEFT JOIN canciones_generos cg ON c.cancion_id = cg.cancion_id
                    LEFT JOIN generos g ON cg.genero_id = g.genero_id
                    LEFT JOIN (
                        SELECT cancion_id, COUNT(*) as total 
                        FROM reacciones_canciones 
                        WHERE tipo = 'like' 
                        GROUP BY cancion_id
                    ) likes ON c.cancion_id = likes.cancion_id
                    LEFT JOIN (
                        SELECT cancion_id, COUNT(*) as total 
                        FROM reacciones_canciones 
                        WHERE tipo = 'dislike' 
                        GROUP BY cancion_id
                    ) dislikes ON c.cancion_id = dislikes.cancion_id
                    LEFT JOIN reacciones_canciones rc ON c.cancion_id = rc.cancion_id 
                        AND rc.usuario_id = %s
                    WHERE (
                        c.titulo LIKE %s 
                        OR ar.nombre LIKE %s 
                        OR g.nombre LIKE %s
                        OR a.titulo LIKE %s
                    )
                    ORDER BY c.titulo LIMIT 50
                """
                
                termino_like = f'%{termino}%'
                params = [usuario_id, termino_like, termino_like, termino_like, termino_like]

                cursor.execute(query, params)
                resultados = cursor.fetchall()
                
                print(f"✅ {len(resultados)} canciones encontradas")
                
                canciones = []
                for cancion in resultados:
                    duracion = str(cancion[2]) if cancion[2] else "0:00"
                    if len(duracion) > 5:
                        duracion = duracion[3:8]
                    
                    canciones.append({
                        'id': cancion[0],
                        'titulo': cancion[1],
                        'duracion': duracion,
                        'ruta_archivo': cancion[3],
                        'album': cancion[4] if cancion[4] else 'Sin álbum',
                        'portada': cancion[5] if cancion[5] else 'https://via.placeholder.com/150',
                        'artista': cancion[6] if cancion[6] else 'Artista desconocido',
                        'genero': cancion[7] if cancion[7] else 'Sin género',
                        'likes': int(cancion[8]),
                        'dislikes': int(cancion[9]),
                        'reaccion_usuario': cancion[10]
                    })
                
                return JsonResponse({
                    'success': True,
                    'canciones': canciones,
                    'total': len(canciones)
                })
                
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'message': str(e)
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

def servir_audio(request, ruta):
    """Sirve archivos de audio de manera segura"""
    try:
        # Construir la ruta completa
        if ruta.startswith('canciones/'):
            # Si está en MEDIA_ROOT/canciones/
            file_path = os.path.join(settings.MEDIA_ROOT, ruta)
        elif ruta.startswith('media/'):
            # Si está en static/interfaz/media/
            file_path = os.path.join(settings.BASE_DIR, 'interfaz', 'static', 'interfaz', ruta)
        else:
            return Http404("Ruta no válida")
        
        # Verificar que el archivo existe
        if not os.path.exists(file_path):
            raise Http404("Archivo no encontrado")
        
        # Servir el archivo
        response = FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_path)}"'
        return response
        
    except Exception as e:
        print(f"Error al servir audio: {e}")
        raise Http404("Error al acceder al archivo")
    
@csrf_exempt
def reaccionar_cancion(request):
    """Vista para manejar likes/dislikes de canciones"""
    if request.method == 'POST':
        try:
            # Verificar si hay sesión activa
            if 'usuario_id' not in request.session:
                return JsonResponse({
                    'success': False,
                    'message': 'Debes iniciar sesión para reaccionar'
                })
            
            data = json.loads(request.body)
            cancion_id = data.get('cancion_id')
            tipo_reaccion = data.get('tipo')  # 'like' o 'dislike'
            usuario_id = request.session['usuario_id']
            
            print(f"🎵 Usuario {usuario_id} reaccionando a canción {cancion_id} con {tipo_reaccion}")
            
            if tipo_reaccion not in ['like', 'dislike']:
                return JsonResponse({
                    'success': False,
                    'message': 'Tipo de reacción inválido'
                })
            
            with connection.cursor() as cursor:
                # Verificar si ya existe una reacción
                cursor.execute("""
                    SELECT tipo FROM reacciones_canciones 
                    WHERE usuario_id = %s AND cancion_id = %s
                """, [usuario_id, cancion_id])
                
                reaccion_existente = cursor.fetchone()
                
                if reaccion_existente:
                    tipo_actual = reaccion_existente[0]
                    
                    if tipo_actual == tipo_reaccion:
                        # Si es la misma reacción, ELIMINARLA (toggle off)
                        cursor.execute("""
                            DELETE FROM reacciones_canciones 
                            WHERE usuario_id = %s AND cancion_id = %s
                        """, [usuario_id, cancion_id])
                        print(f"❌ Reacción {tipo_reaccion} eliminada")
                        accion = 'eliminada'
                    else:
                        # Si es diferente, ACTUALIZARLA (cambiar de like a dislike o viceversa)
                        cursor.execute("""
                            UPDATE reacciones_canciones 
                            SET tipo = %s, fecha_reaccion = NOW()
                            WHERE usuario_id = %s AND cancion_id = %s
                        """, [tipo_reaccion, usuario_id, cancion_id])
                        print(f"🔄 Reacción cambiada de {tipo_actual} a {tipo_reaccion}")
                        accion = 'cambiada'
                else:
                    # No existe reacción, CREARLA
                    cursor.execute("""
                        INSERT INTO reacciones_canciones (usuario_id, cancion_id, tipo)
                        VALUES (%s, %s, %s)
                    """, [usuario_id, cancion_id, tipo_reaccion])
                    print(f"✅ Nueva reacción {tipo_reaccion} agregada")
                    accion = 'agregada'
                
                # Obtener contadores actualizados
                cursor.execute("""
                    SELECT 
                        SUM(CASE WHEN tipo = 'like' THEN 1 ELSE 0 END) as likes,
                        SUM(CASE WHEN tipo = 'dislike' THEN 1 ELSE 0 END) as dislikes
                    FROM reacciones_canciones
                    WHERE cancion_id = %s
                """, [cancion_id])
                
                contadores = cursor.fetchone()
                likes = contadores[0] if contadores[0] else 0
                dislikes = contadores[1] if contadores[1] else 0
                
                # Verificar reacción actual del usuario
                cursor.execute("""
                    SELECT tipo FROM reacciones_canciones 
                    WHERE usuario_id = %s AND cancion_id = %s
                """, [usuario_id, cancion_id])
                
                reaccion_actual = cursor.fetchone()
                reaccion_usuario = reaccion_actual[0] if reaccion_actual else None
                
                print(f"📊 Contadores: {likes} likes, {dislikes} dislikes")
                
                return JsonResponse({
                    'success': True,
                    'accion': accion,
                    'likes': likes,
                    'dislikes': dislikes,
                    'reaccion_usuario': reaccion_usuario,
                    'message': f'Reacción {accion} exitosamente'
                })
                
        except Exception as e:
            print(f"❌ Error al procesar reacción: {e}")
            import traceback
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Método no permitido'
    })   