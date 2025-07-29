# Sistema Contable - Django

## Configuración del Proyecto

### Requisitos Previos
- Python 3.8 o superior
- Git

### Instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd sistemagerardo/SistemaContable
```

2. **Crear entorno virtual**
```bash
python -m venv venv_new
```

3. **Activar entorno virtual**
```bash
# Windows
venv_new\Scripts\activate

# Linux/Mac
source venv_new/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Ejecutar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

### Ejecutar el Proyecto

```bash
python manage.py runserver
```

El servidor estará disponible en: http://127.0.0.1:8000/

### Estructura del Proyecto

- `oficont/` - Configuración principal de Django
- `usuarios/` - Aplicación de gestión de usuarios
- `templates/` - Plantillas HTML
- `static/` - Archivos estáticos (CSS, JS, imágenes)

### Funcionalidades

- Sistema de autenticación de usuarios
- Restablecimiento de contraseñas
- Diseño personalizado OFICONT
- Interfaz moderna y responsiva

### Comandos Útiles

```bash
# Verificar estado del proyecto
python manage.py check

# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test

# Shell de Django
python manage.py shell
```

### Notas Importantes

- Asegúrate de tener el entorno virtual activado antes de ejecutar cualquier comando
- El archivo `db.sqlite3` contiene la base de datos local
- Los archivos estáticos se encuentran en la carpeta `static/` 