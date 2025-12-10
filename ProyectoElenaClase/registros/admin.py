from django.contrib import admin
from .models import Alumnos
from .models import Comentarios
from .models import ComentariosContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de permisos "usuarios"
        if request.user.groups.filter(name='Usuarios').exists():
            #bloquea los campos 
            return('matricula','carrera','turno')
            #cualquier otro usuario que no pertenezca al grupo "usuarios"
        else:
            #bloquea los campos 
            return('created', 'updated')


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierachy = 'created'
    radonly_fields = ('created','id')

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id', 'created')
    date_hierachy = 'created'
    radonly_fields = ('created','id')

admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentarios, AdministrarComentarios)
admin.site.register(ComentariosContacto, AdministrarComentariosContacto)