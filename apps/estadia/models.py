from django.db import models

# Create your models here.

mes_choices = [
    ('Enero', 'Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril', 'Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio', 'Julio'),
    ('Agosto', 'Agosto'),
    ('Septiempre', 'Septiembre'),
    ('Octubre', 'Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre'),
]

asignatura_choices = [
    ('Integradora I', 'Integradora I'),
    ('Integradora II', 'Integradora II'),
    ('Integradora III', 'Integradora III'),
    ('Integradora IV', 'Integradora IV'),
    ('Estadia TSU', 'Estadia TSU'),
    ('Estadia ING', 'Estadia ING'),
]

Apersona = [
    ('Asesor', 'Asesor'),
    ('Asesor Empresarial', 'Asesor Empresarial'),
]

Alpersona = [
    ('Tecnico Superior Universitario', 'Tecnico Superior Universitario'),
    ('Ingenieria', 'Ingenieria'),
]

# //////////////////////////////////////////////////////////////

class categoria(models.Model):
    tipo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=254)

    class Meta:
        ordering = ["tipo"]
        verbose_name_plural = "Categoria"

    def __unicode__(self):  # __unicode__ en Python 2
        return '%s' % (self.tipo)


# //////////////////////////////////////////////////////////////

class ciclos(models.Model):
    generacion = models.PositiveIntegerField()
    mes_ini = models.CharField(max_length=80, choices=mes_choices)
    ano_ini = models.CharField(max_length=80)
    mes_fin = models.CharField(max_length=80, choices=mes_choices)
    ano_fin = models.CharField(max_length=80)

    class Meta:
        ordering = ["generacion"]
        verbose_name_plural = "Ciclos"

    def __unicode__(self):  # __unicode__ en Python 2
        return '%s' % (self.generacion)


# //////////////////////////////////////////////////////////////
class asesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo = models.CharField(max_length=25, choices=Apersona)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Asesores"

    def __unicode__(self):  # __unicode__ en Python 2
        return '%s %s' % (self.nombre, self.apellidos)


# //////////////////////////////////////////////////////////////
class alumno(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    tipo = models.CharField(max_length=25, choices=Alpersona)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Alumnos"

    def __unicode__(self):  # __unicode__ en Python 2
        return '%s %s' % (self.nombre, self.apellidos)


# //////////////////////////////////////////////////////////////

class proyecto(models.Model):
    titulo = models.CharField(max_length=25)
    alumno = models.ManyToManyField(alumno)
    asesor = models.ForeignKey(asesor)
    categoria = models.ForeignKey(categoria)
    generacion = models.ForeignKey(ciclos)
    asignatura = models.CharField(max_length=30, choices=asignatura_choices)
    estatus = models.BooleanField(default=True)
    f_publicacion = models.CharField( max_length=10)
    resumenes = models.CharField(max_length=500)
    archivo = models.FileField()

    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "Proyectos"

    def __unicode__(self):  # __unicode__ en Python 2
        return '%s' % (self.titulo)
        # //////////////////////////////////////////////////////////////
