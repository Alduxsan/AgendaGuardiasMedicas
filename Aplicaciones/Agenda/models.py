from django.db import models
from django.contrib.auth.models import User

class CentroSalud(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True)
    departamento = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    emailSupervisor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    
    DEPARTAMENTOS = [
        ('S/A','S/A'),
        ('Artigas','Artigas'), ('Canelones' , 'Canelones'),('Cerro Largo', 'Cerro Largo'),('Colonia','Colonia'),('Durazno','Durazno'),
        ('Flores','Flores'),('Florida','Florida'),('Lavalleja','Lavalleja'),('Maldonado','Maldonado'),('Montevideo','Montevideo'),
        ('Paysandu','Paysandu'),('Rio Negro','Rio Negro'),('Rivera','Rivera'),('Rocha','Rocha'),('Salto','Salto'),('San José','San José'),
        ('Tacuarembó','Tacuarembó'),('Treinta y Trees','Treinta y Tres')  
    ]
    Nombre_Apellido = models.CharField(max_length=30, default="QuimeraDevs") 
    ci = models.IntegerField(primary_key=True)
    ranking = models.IntegerField(default=0)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='usuario')
    nroCaja = models.IntegerField()
    telefono = models.IntegerField()
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTOS, default='S/A')    
    direccion = models.CharField(max_length=30, default='S/A')
    imagen = models.ImageField(blank=True)

    def __str__(self):
        return str(self.usuario)

class Guardia(models.Model):
    DEPARTAMENTOS = [
        ('S/A','S/A'),
        ('Artigas','Artigas'), ('Canelones' , 'Canelones'),('Cerro Largo', 'Cerro Largo'),('Colonia','Colonia'),('Durazno','Durazno'),
        ('Flores','Flores'),('Florida','Florida'),('Lavalleja','Lavalleja'),('Maldonado','Maldonado'),('Montevideo','Montevideo'),
        ('Paysandu','Paysandu'),('Rio Negro','Rio Negro'),('Rivera','Rivera'),('Rocha','Rocha'),('Salto','Salto'),('San José','San José'),
        ('Tacuarembó','Tacuarembó'),('Treinta y Trees','Treinta y Tres')  
    ]
 
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    turno = models.CharField(max_length=25)
    centroSalud = models.ForeignKey(CentroSalud,to_field='nombre',on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING, default=0, blank = True, null = True)
    disponible = models.BooleanField(default=True)
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTOS, default='S/A')
    min_ranking = models.BigIntegerField(blank=False, null=False, default=1)


    def __str__(self):
        return f"{self.id}) {self.centroSalud} {self.turno} {self.fecha} ----> {self.medico} / disponible: {self.disponible}"

    def save(self, *args, **kwargs):
        
        if self.medico != None:
            self.disponible = False
        else:
            self.disponible = True
        
        
        super().save(*args, **kwargs)

class Fecha(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)
