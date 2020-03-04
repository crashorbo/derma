from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet

# Create your models here.

class MyModelMixin(object):
    def q_for_search_word(self, word):
        return Q(nombres__icontains=word) | Q(apellidos__icontains=word) | Q(documento__icontains=word) | Q(nro_documento__icontains=word) | Q(telefono__icontains=word)

    def q_for_search(self, search):
        q = Q()
        if search:
            searches = search.split()
            for word in searches:
                q = q & self.q_for_search_word(word)
        return q

    def filter_on_search(self, search):
        return self.filter(self.q_for_search(search))


class MyModelQuerySet(QuerySet, MyModelMixin):
    pass


class MyModelManager(models.Manager, MyModelMixin):
    def get_queryset(self):
        return MyModelQuerySet(self.model, using=self._db)

DOCUMENTO_CHOICE = (
    (1, 'CEDULA DE IDENTIDAD'),
    (2, 'PASAPORTE'),
    (3, 'CERTIFICADO DE NACIMIENTO')
)

class Paciente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now=True)
    documento = models.IntegerField(choices=DOCUMENTO_CHOICE, default=1)
    nro_documento = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ocupacion = models.CharField(max_length=50, blank=True)
    codigo = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    objects = MyModelManager()