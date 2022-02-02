from django.db import models
from django.utils import timezone
from datetime import datetime   

#Primer Sprint 
class estado(models.Model):
	est_id =  models.CharField('Estado_id', primary_key=True,max_length=40, blank=False,default="0")
	est_nom = models.CharField('Nombre_Secretariado',max_length=20,blank=False)

class carrera(models.Model):
	carr_codigo = models.IntegerField('Codigo_Carrera',primary_key=True,blank=False,default="0")
	carr_nombre = models.CharField('Nombre_Carrera',max_length=50, blank=False)

class asignatura(models.Model):
	Asig_cod = models.IntegerField('Codigo_Asignatura',primary_key=True,blank=False,default="0")
	Asig_nombre = models.CharField('Nombre_Asignatura',max_length=50, blank=False)
	Asig_niv = models.IntegerField('Nivel_Asignatura',blank=False)
	Asig_car = models.ForeignKey(carrera, on_delete=models.CASCADE,default="0")

class estudiante(models.Model):
	Est_Rut = models.CharField('Rut_Estudiante',primary_key=True,max_length=8,blank=False)
	Est_Nom = models.CharField('Nombre_Estudiante',max_length=20,blank=False)
	Est_Ap = models.CharField('Apellido_Estudiante',max_length=20,blank=False)
	Est_Email = models.EmailField('Email_Estudiante',max_length=254,blank=False)
	Est_Tel = models.IntegerField('Telefono_Estudiante',blank=False)
	Est_Contrasena = models.CharField('Contraseña_Estudiante',max_length=8,blank=False)
	Est_Carr_codigo = models.ForeignKey(carrera, on_delete=models.CASCADE,default="0")
	def __str__(self):				#Funcion de llamada o que se muestra en admin dejo de ejemplo para implementar funciones por objeto o clase
		return self.Est_Rut

class solicitud(models.Model):
	Sol_fecha = models.DateTimeField('Solicitud_fecha', default=datetime.now, blank=False)
	Sol_id = models.BigIntegerField('Solicitud_id', primary_key=True, blank=False)
	Sol_rut = models.ForeignKey(estudiante, on_delete=models.CASCADE)
	Sol_estado = models.ForeignKey(estado, on_delete=models.CASCADE)
	Sol_semestre = models.CharField('Solicitud_semestre', max_length=500,blank=False)
	###Sol_estado = models.CharField('Solicitud_estado',max_length=10, blank=False)###LLega como forean key
	Sol_motivo = models.CharField('Solicitud_motivo', max_length=500,blank=False)
	class Meta:
		abstract = True        

class por_tope(solicitud):                                                                       # cambie models.model por models.solicitud por herencia (no estoy seguro)
	Tope_id_asig_ins = models.ForeignKey(asignatura, on_delete=models.CASCADE, related_name='id_a_inscribir')                   # cambie'_asignatura' a '_asig_ins'
	Tope_id_asig_tope = models.ForeignKey(asignatura, on_delete=models.CASCADE, related_name='id_tope_horario')  		            # cambie '_inscribir' a '_id_asig' ademas de volverlo un integerfield
	
class sin_requisito(solicitud):                                                                  # cambie models.model por models.solicitud por herencia (no estoy seguro)
	sin_req_id_asig_ins = models.ForeignKey(asignatura, on_delete=models.CASCADE)  


class operacion(models.Model):
	ope_id = models.IntegerField('Id_Operacion',primary_key=True,blank=False)
	ope_nombre = models.CharField('Nombre_Operacion',max_length=50, blank=False)
class mensaje(models.Model):
	men_id = models.BigIntegerField('Id_Mensaje',primary_key=True,blank=False)
	men_nombre = models.CharField('Nombre_Mensaje',max_length=50, blank=False)
	men_ope = models.ForeignKey(operacion, on_delete=models.CASCADE)

#Segundo Sprint

class secretariado(models.Model):
	Sec_Rut = models.CharField('Rut_Secretariado',primary_key=True,max_length=8,blank=False)
	Sec_Nom = models.CharField('Nombre_Secretariado',max_length=20,blank=False)
	Sec_Ap = models.CharField('Apellido_Secretariado',max_length=20,blank=False)
	Sec_Email = models.EmailField('Email_Secretariado',max_length=254,blank=False)
	Sec_Tel = models.IntegerField('Telefono_Secretariado',blank=False)
	Sec_Contrasena = models.CharField('Contraseña_Secretariado',max_length=20,blank=False)
	Sec_car = models.ForeignKey(carrera, on_delete=models.CASCADE,default="0")



