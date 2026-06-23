from django.db import models
from leads.models import Lead

class NotaCRM(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "crm_notas"

class RecordatorioCRM(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    fecha_recordatorio = models.DateTimeField()
    completado = models.BooleanField(default=False)

    class Meta:
        db_table = "crm_recordatorios"

class Pipeline(models.Model):
    ESTADOS = [
        ("nuevo", "Nuevo"),
        ("proceso", "En proceso"),
        ("cerrado", "Cerrado"),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="nuevo")
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "crm_pipeline"
def __str__(self):
        return f"{self.titulo} ({self.lead})"