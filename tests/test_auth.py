from django.test import TestCase, Client
from django.urls import reverse
from .models import Usuario
from django.contrib.auth.hashers import make_password

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Creamos usuario con contraseña hasheada real
        self.usuario = Usuario.objects.create(
            nombre="Test",
            email="test@test.com",
            contrasena=make_password("12345") # Importante hashear
        )

    def test_AUTH_03_login_manual(self):
        url = reverse('login_view') # Asegúrate que tu url se llame así
        data = {
            'email': 'test@test.com',
            'password': '12345'
        }
        response = self.client.post(url, data)
        
        # 1. Verificar redirección
        self.assertRedirects(response, reverse('home'))
        
        # 2. Verificar que TU lógica de sesión funcionó
        # OJO: Aquí verificamos la sesión del cliente de prueba
        session = self.client.session
        self.assertEqual(session['usuario_email'], 'test@test.com')
        self.assertIsNotNone(session.get('usuario_id'))