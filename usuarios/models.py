from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('contador', 'Contador'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
