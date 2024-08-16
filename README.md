Proyecto Final Bogado
Este es un proyecto de blog orientado a juegos desarrollado con Django. El objetivo es proporcionar una plataforma donde los usuarios puedan crear, editar, y ver publicaciones relacionadas con juegos.

Funcionalidades:

Autenticación de Usuarios: Los usuarios pueden registrarse e iniciar sesión para acceder a funcionalidades exclusivas.

Creación de Publicaciones: Los usuarios autenticados pueden crear nuevas publicaciones sobre juegos, incluyendo un subtítulo y detalles sobre el creador.

Lista de Publicaciones: Visualiza una lista de todas las publicaciones disponibles.

Detalles de Publicación: Cada publicación tiene una página de detalles que muestra el contenido completo.

publicacion_view: Los creadores pueden editar sus propias publicaciones.

publicacion_confirm_delete: Una confirmacion para advertir a los super user de borrar la publicacion.

other_styles.css: Utiliza un archivo de estilos (other_styles.css) para la apariencia del blog.


Instalación
Clona el repositorio:

bash
Copiar código
git clone https://github.com/Emanu77-python/Proyecto-Final-Bogado.git
Navega al directorio del proyecto:

bash
Copiar código
cd Proyecto-Final-Bogado
Crea un entorno virtual y actívalo:

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Realiza las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate
Crea un superusuario (opcional, para administración):

bash
Copiar código
python manage.py createsuperuser
Ejecuta el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Abre tu navegador y accede a:

arduino
Copiar código
http://127.0.0.1:8000/

