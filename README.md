# Proyecto Django: Sistema de Gestión de Hotel

Este proyecto es un sistema básico para la gestión de huéspedes y reservas de hotel utilizando Django como framework y PostgreSQL como base de datos. Incluye configuración inicial, modelos de base de datos, vistas, plantillas y ejemplos de datos cargados a través del shell interactivo de Django.

## Tecnologías utilizadas

- **Django**: Framework web en Python.
- **PostgreSQL**: Base de datos relacional.

## Configuración inicial

1. **Crear el proyecto y la aplicación**

   Ejecuta los siguientes comandos para configurar el entorno:
   ```bash
   django-admin startproject hotel_manager
   cd hotel_manager
   python manage.py startapp booking
   ```

2. **Instalar el conector para PostgreSQL**

   Instala el paquete `psycopg2` para conectar Django con PostgreSQL:
   ```bash
   pip install psycopg2
   ```

3. **Configurar la base de datos**

   Modifica el archivo `hotel_manager/settings.py` para configurar PostgreSQL:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'hotel_db',
           'USER': 'hotel_user',
           'PASSWORD': 'securepassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Agregar la aplicación `booking` al proyecto**

   En el archivo `hotel_manager/settings.py`, añade `booking` al listado de aplicaciones instaladas:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'booking',
   ]
   ```

## Modelos

Define los modelos de la aplicación en el archivo `booking/models.py`:
```python
from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    room_number = models.CharField(max_length=5)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.guest.first_name} {self.guest.last_name}"
```

## Migraciones

1. **Crear y aplicar migraciones**

   Ejecuta los siguientes comandos para reflejar los modelos en la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Vistas

Define las vistas en el archivo `booking/views.py`:
```python
from django.shortcuts import render
from .models import Guest, Reservation

def list_guests(request):
    guests = Guest.objects.all()
    return render(request, 'list_guests.html', {'guests': guests})

def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'list_reservations.html', {'reservations': reservations})
```

## URLs

Configura las rutas principales en el archivo `hotel_manager/urls.py`:
```python
from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guests/', views.list_guests, name='list_guests'),
    path('reservations/', views.list_reservations, name='list_reservations'),
]
```

## Plantillas

**list_guests.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Guest List</title>
</head>
<body>
    <h1>Guest List</h1>
    <ul>
        {% for guest in guests %}
            <li>{{ guest.first_name }} {{ guest.last_name }} - {{ guest.email }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**list_reservations.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Reservations List</title>
</head>
<body>
    <h1>Reservations</h1>
    <ul>
        {% for reservation in reservations %}
            <li>Room {{ reservation.room_number }}: {{ reservation.guest.first_name }} {{ reservation.guest.last_name }} (Check-in: {{ reservation.check_in }}, Check-out: {{ reservation.check_out }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Carga de datos desde el shell

1. **Abrir el shell interactivo de Django**
   ```bash
   python manage.py shell
   ```

2. **Insertar datos iniciales**
   ```python
   from booking.models import Guest, Reservation
   from datetime import date

   # Crear huéspedes
   guest1 = Guest.objects.create(first_name="Alice", last_name="Johnson", email="alice@example.com", phone="1234567890")
   guest2 = Guest.objects.create(first_name="Bob", last_name="Smith", email="bob@example.com", phone="0987654321")

   # Crear reservas
   Reservation.objects.create(room_number="101", check_in=date(2024, 12, 15), check_out=date(2024, 12, 20), guest=guest1, total_price=500.00)
   Reservation.objects.create(room_number="102", check_in=date(2024, 12, 16), check_out=date(2024, 12, 21), guest=guest2, total_price=600.00)
   ```

## Ejecutar el servidor

Para iniciar el servidor y probar las rutas configuradas:
```bash
python manage.py runserver
```

Rutas disponibles:
- **Lista de huéspedes:** [http://localhost:8000/guests/](http://localhost:8000/guests/)
- **Lista de reservas:** [http://localhost:8000/reservations/](http://localhost:8000/reservations/)

## Conclusión

Este proyecto demuestra:
1. Configuración de Django con PostgreSQL.
2. Creación de modelos para gestionar huéspedes y reservas.
3. Consultas básicas y avanzadas utilizando el ORM de Django.
4. Carga inicial de datos a través del shell interactivo.

Es un punto de partida ideal para desarrollar sistemas de gestión hotelera más avanzados. Si tienes preguntas, ¡no dudes en preguntar!

