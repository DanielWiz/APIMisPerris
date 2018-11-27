from django.db import models

class PerrosRescatados(models.Model):
    Fotografia = models.ImageField(upload_to="Usuarios/media/imagenesPerros/")
    NombrePerro = models.CharField(max_length=200)
    RazaPredominante = models.CharField(max_length=200)
    Descripcion = models.TextField()
    ESTADOS = (('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
    Estado = models.CharField(max_length=1,choices=ESTADOS,default='R')
    
    def __str__(self):
        return self.NombrePerro
