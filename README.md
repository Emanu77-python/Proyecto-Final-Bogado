Proyecto Final Bogado:
Este es un proyecto de blog orientado a juegos desarrollado con Django. El objetivo es proporcionar una plataforma donde los usuarios puedan crear, editar, y ver publicaciones relacionadas con juegos.

Funcionalidades:

index.html: la base de todo , en si la pagina web.

inicio_no_autenticado:un mensaje para cuando entres a crear/ osea la pagina para crear publicaciones y no estes autenticado: " Necesitas iniciar sesión para crear una publicación. Inicia sesión aquí".

sign_up: html para registrarse.

login: html para logearse (iniciar sesion)

about_me: un html que cuenta cosas sobre mí.

crear_publicacion: Los usuarios autenticados pueden crear nuevas publicaciones sobre juegos, incluyendo un subtítulo y detalles sobre el creador.

publicacion_list: Visualiza una lista de todas las publicaciones disponibles.

publicacion_detail: Cada publicación tiene una página de detalles que muestra el contenido completo.

publicacion_view: Los creadores pueden editar sus propias publicaciones.

publicacion_confirm_delete: Una confirmacion para advertir a los super user de borrar la publicacion.

other_styles.css: Utiliza un archivo de estilos (other_styles.css) para la apariencia del blog.

carpeta "media": una carpeta para guardar las imagenes puestas en las publicaciones.


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

