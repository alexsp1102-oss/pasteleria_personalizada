from django.db import models

class Lead(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico = models.CharField(max_length=100)
    tipo_evento = models.CharField(max_length=50, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    numero_personas = models.IntegerField(blank=True, null=True)
    sabor_interes = models.CharField(max_length=50, blank=True, null=True)
    tamano = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    entrega_domicilio = models.BooleanField(default=False)
    acepta_privacidad = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "leads"

    def __str__(self):
        return self.nombre_completo

class Meta:
    db_table = "leads"
class Meta:
    db_table = "leads"
    managed = False
