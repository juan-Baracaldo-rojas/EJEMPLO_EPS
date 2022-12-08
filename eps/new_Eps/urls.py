from django.urls import path
from . import views 

urlpatterns = [
    path("",views.inicio, name="inicio"),
    path('index',views.index, name="index"),

    # URLS CREAR
    path('createDoctor',views.createDoctor, name="createDoctor"),
    path('createUser',views.createUser, name="createUser"),
    path('createAppointment',views.createAppointment, name="createAppointment"),

    # URLS ACTUALIZAR
    path('updateDoctor',views.updateDoctor, name="updateDoctor"),
    path('updateUser',views.updateUser, name="updateUser"),
    path('updateAppointment',views.updateAppointment, name="updateAppointment"),

    path('updateDoctor/<int:id>',views.updateDoctor, name="updateDoctor"),
    path('updateUser/<int:id>',views.updateUser, name="updateUser"),
    path('updateAppointment/<int:id>',views.updateAppointment, name="updateAppointment"),

    # URLS VER
    path('readDoctors',views.readDoctors, name="readDoctors"),
    path('readUsers',views.readUsers, name="readUsers"),
    path('readAppointment',views.readAppointment, name="readAppointment"),

    #URL BORRAR
    path('deleteDoctor/<int:id>',views.deleteDoctor,name='deleteDoctor'),
    path('deleteUsers/<int:id>',views.deleteUsers, name='deleteUsers'),
    path('deleteAppointment/<int:id>',views.deleteAppointment, name='deleteAppointment'),
    
    # URLS ABOUT
    path('about',views.about, name="about")

]
