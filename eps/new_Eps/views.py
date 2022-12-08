from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Appointment,Doctor
from .forms import AppointmentForm,UserForm,DoctorForm
# Create your views here.

# vistas de inicial
def inicio(request):
    return HttpResponse("<h1>Estoy vivo</h1>")

# vista de index
def index(request):
    return render(request,'Pages/index.html')

# vistas de crear
def createAppointment(request):
    formAppointment=AppointmentForm(request.POST or None,request.FILES or None)
    print(formAppointment.fields.items())
    if formAppointment.is_valid():
        formAppointment.save()
        return redirect('readAppointment')
    else:
        print('no es valido')
    return render(request,"pagesAppointments/createAppointment.html",{'formAppointment':formAppointment})

def createDoctor(request):
    formDoctor=DoctorForm(request.POST or None,request.FILES or None)
    if formDoctor.is_valid():
        formDoctor.save()
        return redirect('readDoctors')
    return render(request,"pagesDoctors/createDoctor.html",{'formDoctor':formDoctor})

def createUser(request):
    formUser=UserForm(request.POST or None,request.FILES or None)
    if formUser.is_valid():
        formUser.save()
        return redirect('readUsers')
    return render(request,"pagesUsers/createUser.html",{'formUser':formUser})

# vistas de actualizar
def updateAppointment(request,id):
    appointment=Appointment.objects.get(id=id)
    formAppointment=AppointmentForm(request.POST or None, request.FILES or None, instance=appointment)
    if formAppointment.is_valid() and request.POST:
        formAppointment.save()
        return redirect('readAppointment')
    return render(request,'pagesAppointments/updateAppointment.html',{'formAppointment':formAppointment})

def updateDoctor(request,id):
    doctor=Doctor.objects.get(id=id)
    formDoctor=DoctorForm(request.POST or None,request.FILES or None,instance=doctor)
    if formDoctor.is_valid() and request.POST:
        formDoctor.save()
        return redirect('readDoctors')
    return render(request,"pagesDoctors/updateDoctor.html",{'formDoctor':formDoctor})

def updateUser(request,id):
    user=User.objects.get(id=id)
    formUser=UserForm(request.POST or None,request.FILES or None,instance=user)
    if formUser.is_valid() and request.POST:
        formUser.save()
        return redirect('readUsers')
    return render(request,"pagesUsers/updateUser.html",{'formUser':formUser})

# vistas de lectura
def readDoctors(request):
    doctors=Doctor.objects.all()
    return render(request,"pagesDoctors/readDoctors.html",{'doctors':doctors})

def readUsers(request):
    users=User.objects.all()
    return render(request,"pagesUsers/readUser.html",{'users':users})

def readAppointment(request):
    appointments=Appointment.objects.all()
    return render(request,"pagesAppointments/readAppointment.html",{'appointments':appointments})

# vistas de eliminar
def deleteDoctor(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('readDoctors')

def deleteUsers(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('readUsers')

def deleteAppointment(request,id):
    appointment=Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('readAppointment')

# vista about
def about(request):
    return render(request,"Pages/about.html")