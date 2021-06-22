from django.db import models
 # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.

class Categoria(models.Model):
	idCategoria = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)


	def __str__(self):
		"""String for representing the Model object."""
		return self.nombre

class Donacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreObjeto = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=False)
    descripcion = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        #return f'{self.id} ({self.title})'
        return self.nombreObjeto


    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/img1.jpng')