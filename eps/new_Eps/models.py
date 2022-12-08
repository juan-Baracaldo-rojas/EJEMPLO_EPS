from tabnanny import verbose
from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name="Nombre")
    n_Consultorio=models.IntegerField(verbose_name="N_Consultorio")
    especialidad=models.CharField(max_length=100,verbose_name="Especialidad")
    celular=models.BigIntegerField(verbose_name='Celular')
    password=models.CharField(max_length=100,verbose_name='Password')

    def __str__(self):
        return str('Nombre Doctor: {} - Especialidad:{} '.format(self.nombre,self.especialidad))

class User(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,verbose_name='Nombre')
    apellidos=models.CharField(max_length=100,verbose_name='Apellidos')
    celular=models.BigIntegerField(verbose_name='Celular')
    email=models.CharField(max_length=150,verbose_name='Email')
    direccion=models.CharField(max_length=100,verbose_name='Direccion')
    edad=models.IntegerField(verbose_name='Edad')
    sede=models.CharField(max_length=100,verbose_name='Sede')
    tipo_Usuario=models.CharField(max_length=100,verbose_name='Tipo_Usuario')
    tipo_Contrato=models.CharField(max_length=100,verbose_name='Tipo_Contrato')
    plan=models.CharField(max_length=100,verbose_name='Plan')
    
    def __str__(self):
        return str('Nombre Usuario: {} - Apellido:{} - Sede {} - Tipo Contrato{}'.format(self.nombre,self.apellidos,self.sede,self.tipo_Contrato))

class Appointment(models.Model):
    id=models.AutoField(primary_key=True)
    fecha_Cita=models.DateField(verbose_name='Fecha_Cita')
    id_Usuario=models.IntegerField(verbose_name='Id_Usuario')
    n_Consultorio=models.IntegerField(verbose_name='N_Consultorio')
    nombre_Doctor=models.CharField(max_length=100,verbose_name='Nombre_Doctor' )
    especialidad_Doctor=models.CharField(max_length=100,verbose_name='Especialidad_Doctor')
    modalidad=models.CharField(max_length=100,verbose_name='Modalidad' )
    estado=models.CharField(max_length=100,verbose_name='Estado')

    def __str__(self):
        return str("Id Cita: {} - Id Usuario: {} - Estado: {}".format(self.id,  self.id_Usuario,  self.estado,))
        