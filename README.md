Hola! Bienvenidos a este Proyecto! en este README explicare las funcionalidades de este proyecto:

MODELS:

clase: Publicacion:
titulo = models.CharField(max_length=200) --> el titulo de la publicacion. Charfield para que el titulo pueda ingresarse como texto, y el max_length =200 Seria el limite de carácteres que puede tener el titulo.
    subtitulo = models.CharField(max_length=200, blank=True, null=True) lo mismo que titulo, solo varia el nombre.
    contenido = models.TextField(), Casi lo mismo que lo anterior, pero la diferencia es el TEXTFIELD que es para que el usuario ingrese el contenido sin limitaciones, osea , escribir todo lo que quiera.
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)