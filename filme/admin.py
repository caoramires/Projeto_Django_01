from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# inlcusão do campo personalizado 'filmes_vistos'
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
