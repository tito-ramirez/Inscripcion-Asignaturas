from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views import View
from .models import por_tope
from .models import estudiante
from .models import sin_requisito
from .models import asignatura
from .models import estado
from .models import operacion
from .models import mensaje
from .models import secretariado
from datetime import datetime
import psycopg2 
from django.db.models import Q

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')
def vista1(request): 
	return render(request, 'vista1.html')

class vista1clase(View):
    def get(self, request):
        username = request.user.username
        if request.user.is_staff:
            nombre = secretariado.objects.filter(Sec_Rut=username)
            por_topes = por_tope.objects.all()
            sin_requisitos = sin_requisito.objects.all()
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            if int(id2[1]) < 7:
                semestre = '1-'+str(id2[0])
            else:
                semestre = '2-'+str(id2[0])
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            id_solicitud = id2[0]+id2[1]+id3[1]+id4[0]

            print(id1)
            return render(request, 'vista1.html', {'datos':por_topes,'datos2':sin_requisitos,'nombre':nombre})
        else:
            nombre = estudiante.objects.filter(Est_Rut=username)
            return render(request, 'vista1.html',{'nombre':nombre})
        	
class visualizar_solicitudes_e(View):
    def get(self, request):
        username = request.user.username
        nombre = secretariado.objects.filter(Sec_Rut=username)
        criterion1 = Q(Sol_estado=0)
        criterion2 = Q(Sol_estado=1)
        por_topes = por_tope.objects.filter(criterion1 | criterion2)
        sin_requisitos = sin_requisito.objects.filter(criterion1 | criterion2)
        id1 = datetime.now()
        id1 = str(id1)
        id2 = id1.split('-')
        if int(id2[1]) < 7:
            semestre = '1-'+str(id2[0])
        else:
            semestre = '2-'+str(id2[0])
        id3 = id2[2].split(':')
        id4 = id2[2].split(' ')
        id_solicitud = id2[0]+id2[1]+id3[1]+id4[0]
        print(id1)
        return render(request, 'visualizar_solicitudes.html', {'datos':por_topes,'datos2':sin_requisitos,'nombre':nombre})

class modificarestado_portope(View):
    def get(self, request):
        username = request.user.username
        nombre = secretariado.objects.filter(Sec_Rut=username)
        id_solicitud = request.GET.get('id')
        estado_actual = request.GET.get('estado')
        query = estado.objects.all()
        return render(request, 'modificarestado_portope.html', {'datos':query,'estado':estado_actual,'idsolicitud':id_solicitud,'nombre':nombre})


class modificarestado_por_tope2(View):
    def get(self, request):
        try:
            idsolicitud = request.GET.get('idsolicitud')
            estadonuevo = request.GET.get('estadonuevo')               
            query3 = estado.objects.filter(est_id=int(estadonuevo))
            por_tope.objects.filter(Sol_id=idsolicitud).update(Sol_estado=query3[0])
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            print(id1)
            id11 = id1.split(' ')
            id111 = id11[1].split(':')
            segundos = id111[2].split('.')
            print(segundos)
            id_solicitud2 = segundos[0]+segundos[1]+id111[0]
            query6 = operacion.objects.filter(ope_id=int(3))
            print(query6[0])
            mensaje.objects.create(men_id=id_solicitud2,men_nombre="Operacion_exitosa",men_ope=query6[0])
            ok="ok"
            return render(request, 'vista1.html', {'modificarok':ok})
        except:
            username = request.user.username
            error="ok"
            nombre = secretariado.objects.filter(Sec_Rut=username)
            criterion1 = Q(Sol_estado=0)
            criterion2 = Q(Sol_estado=1)
            por_topes = por_tope.objects.filter(criterion1 | criterion2)
            sin_requisitos = sin_requisito.objects.filter(criterion1 | criterion2)
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            if int(id2[1]) < 7:
                semestre = '1-'+str(id2[0])
            else:
                semestre = '2-'+str(id2[0])
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            id_solicitud = id2[0]+id2[1]+id3[1]+id4[0]
            print(id1)
            return render(request, 'visualizar_solicitudes.html', {'datos':por_topes,'datos2':sin_requisitos,'nombre':nombre,'error':error})
            
            

class modificarestado_sinreq(View):
    def get(self, request):
        username = request.user.username
        nombre = secretariado.objects.filter(Sec_Rut=username)
        id_solicitud = request.GET.get('id')
        estado_actual = request.GET.get('estado')
        query = estado.objects.all()
        return render(request, 'modificarestado_sinreq.html', {'datos':query,'estado':estado_actual,'idsolicitud':id_solicitud,'nombre':nombre})


class modificarestado_sinreq2(View):
    def get(self, request):
        try:
            idsolicitud = request.GET.get('idsolicitud')
            estadonuevo = request.GET.get('estadonuevo')               
            query3 = estado.objects.filter(est_id=int(estadonuevo))
            sin_requisito.objects.filter(Sol_id=idsolicitud).update(Sol_estado=query3[0])
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            print(id1)
            id11 = id1.split(' ')
            id111 = id11[1].split(':')
            segundos = id111[2].split('.')
            print(segundos)
            id_solicitud2 = segundos[0]+segundos[1]+id111[0]
            query6 = operacion.objects.filter(ope_id=int(3))
            print(query6[0])
            mensaje.objects.create(men_id=id_solicitud2,men_nombre="Operacion_exitosa",men_ope=query6[0])
            ok="ok"
            return render(request, 'vista1.html', {'modificarok':ok})
        except:
            username = request.user.username
            error="ok"
            nombre = secretariado.objects.filter(Sec_Rut=username)
            criterion1 = Q(Sol_estado=0)
            criterion2 = Q(Sol_estado=1)
            por_topes = por_tope.objects.filter(criterion1 | criterion2)
            sin_requisitos = sin_requisito.objects.filter(criterion1 | criterion2)
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            if int(id2[1]) < 7:
                semestre = '1-'+str(id2[0])
            else:
                semestre = '2-'+str(id2[0])
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            id_solicitud = id2[0]+id2[1]+id3[1]+id4[0]
            print(id1)
            return render(request, 'visualizar_solicitudes.html', {'datos':por_topes,'datos2':sin_requisitos,'nombre':nombre,'error':error})


class Solicitud_por_tope(View):
    def get(self, request):
        username = request.user.username
        query = estudiante.objects.filter(Est_Rut=username)
        query2 = asignatura.objects.filter(Asig_car=query[0].Est_Carr_codigo.carr_codigo)
        id1 = datetime.now()
        id1 = str(id1)
        id2 = id1.split('-')
        if int(id2[1]) < 7:
            semestre = '1-'+str(id2[0])
        else:
            semestre = '2-'+str(id2[0])
        return render(request, 'Solicitud_tope.html', {'datos':query,'datos2':query2,'semestre':semestre})



class crear_Solicitud_por_tope(View):
    def get(self, request):
        try:
            id_solicitud = request.GET.get('id_solicitud')
            rut = request.GET.get('user_rut')
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            id11 = id1.split(' ')
            id111 = id11[1].split(':')
            segundos = id111[2].split('.')
            print(segundos)
            id_solicitud2 = segundos[0]+segundos[1]+id111[0]
            id_solicitud = segundos[0]+segundos[1]+id111[0]+rut
            rut = int(rut) 
            motivo = request.GET.get('Motivo')
            id_as_ins = request.GET.get('IdAsIns')
            id_as_tope = request.GET.get('IdAsTope')
            semestre = request.GET.get('user_semestre')
            print("hola")
            query3 = estado.objects.all()
            print(query3[0].est_id)
            query4 = asignatura.objects.filter(Asig_cod=id_as_ins)
            query5 = asignatura.objects.filter(Asig_cod=id_as_tope)
            print("/////////")
            query6 = operacion.objects.filter(ope_id=int(0))
            print(query6[0])
            mensaje.objects.create(men_id=id_solicitud2,men_nombre="Operacion_exitosa",men_ope=query6[0])
            por_tope.objects.create(Sol_fecha=datetime.now(), Sol_id=id_solicitud, Sol_rut_id=rut, Sol_estado=query3[0], Sol_motivo=motivo, Tope_id_asig_ins=query4[0], Tope_id_asig_tope=query5[0], Sol_semestre= semestre)
            ok="ok"
            return render(request, 'vista1.html', {'solicitudok':ok})
        except:
            error="ok"            	        
            username = request.user.username
            query = estudiante.objects.filter(Est_Rut=username)
            query2 = asignatura.objects.filter(Asig_car=query[0].Est_Carr_codigo.carr_codigo)
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            if int(id2[1]) < 7:
                semestre = '1-'+str(id2[0])
            else:
                semestre = '2-'+str(id2[0])
            return render(request, 'Solicitud_tope.html', {'datos':query,'datos2':query2,'semestre':semestre,'error':error})
class Solicitud_sin_prerequisito(View):
    def get(self, request):
        username = request.user.username
        query = estudiante.objects.filter(Est_Rut=username)
        query2 = asignatura.objects.filter(Asig_car=query[0].Est_Carr_codigo.carr_codigo)
        id1 = datetime.now()
        id1 = str(id1)
        id2 = id1.split('-')
        if int(id2[1]) < 7:
            semestre = '1-'+str(id2[0])
        else:
            semestre = '2-'+str(id2[0])

        return render(request, 'solicitud_prerequisito.html', {'datos':query,'datos2':query2,'semestre':semestre})	

class crear_Solicitud_sin_requisito(View):
    def get(self, request):
        try:
            id_solicitud = request.GET.get('id_solicitud')
            rut = request.GET.get('user_rut')
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            id3 = id2[2].split(':')
            id4 = id2[2].split(' ')
            id11 = id1.split(' ')
            id111 = id11[1].split(':')
            segundos = id111[2].split('.')
            print(segundos)
            id_solicitud2 = segundos[0]+segundos[1]+id111[0]
            id_solicitud = segundos[0]+segundos[1]+id111[0]+rut
            rut = int(rut) 
            semestre = request.GET.get('user_semestre')
            motivo = request.GET.get('Motivo')
            id_as_ins = request.GET.get('IdAsIns')
            print("hola")
            query3 = estado.objects.all()
            query4 = asignatura.objects.filter(Asig_cod=id_as_ins)
            query6 = operacion.objects.filter(ope_id=int(1))
            print(query6[0])
            mensaje.objects.create(men_id=id_solicitud2,men_nombre="Operacion_exitosa",men_ope=query6[0])
            sin_requisito.objects.create(Sol_fecha=datetime.now(), Sol_id=id_solicitud, Sol_rut_id=rut, Sol_estado=query3[0], Sol_motivo=motivo, sin_req_id_asig_ins=query4[0], Sol_semestre= semestre)
            ok="ok"
            return render(request, 'vista1.html', {'solicitudok':ok})        
        except:
            error="ok"
            username = request.user.username
            query = estudiante.objects.filter(Est_Rut=username)
            query2 = asignatura.objects.filter(Asig_car=query[0].Est_Carr_codigo.carr_codigo)
            id1 = datetime.now()
            id1 = str(id1)
            id2 = id1.split('-')
            if int(id2[1]) < 7:
                semestre = '1-'+str(id2[0])
            else:
                semestre = '2-'+str(id2[0])

            return render(request, 'solicitud_prerequisito.html', {'datos':query,'datos2':query2,'semestre':semestre,'error':error})    

class Ver_solicitudes(View):
    def get(self, request):
        username = request.user.username
        nombre = estudiante.objects.filter(Est_Rut=username)
        query = por_tope.objects.filter(Sol_rut=username)
        query2 = sin_requisito.objects.filter(Sol_rut=username)
        id1 = datetime.now()
        id1 = str(id1)
        id2 = id1.split('-')
        id3 = id2[2].split(':')
        id4 = id2[2].split(' ')
        print(id1)
        id11 = id1.split(' ')
        id111 = id11[1].split(':')
        segundos = id111[2].split('.')
        print(segundos)
        id_solicitud2 = segundos[0]+segundos[1]+id111[0]
        query6 = operacion.objects.filter(ope_id=int(2))
        print(query6[0])
        mensaje.objects.create(men_id=id_solicitud2,men_nombre="Operacion_exitosa",men_ope=query6[0])
        return render(request, 'ver_solicitudes.html',{'datos':query,'datos2':query2,'nombre':nombre})	        
