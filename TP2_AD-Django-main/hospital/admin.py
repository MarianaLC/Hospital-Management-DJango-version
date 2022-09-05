from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from admin_searchable_dropdown.filters import AutocompleteFilter

from .import forms
from .models import *


# from .models import <modelos a serem geridos>
# basicamente tudo o que aparece para o admin ele pode criar medicamentos e assim
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['dci','nome_medicamento', 'forma_farmaceutica', 'dosagem', 'estado_autorizacao', 'generico',
                    'titular_AIM',]
    search_fields = ('nome_medicamento', 'titular_AIM')
    ordering = ('nome_medicamento',)

@admin.register(Outro_Artigo)
class OutroArtigoAdmin(admin.ModelAdmin):
    list_display = ['nome_artigo', 'fornecedor',]
    search_fields = ('nome_artigo', 'fornecedor')
    ordering = ('nome_artigo',)


class UtenteAdmin(UserAdmin):
    form = forms.UtenteChangeForm
    add_form = forms.UtenteCreationForm
    search_fields = ('nome', 'NIF')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'bi', 'NIF','morada', 'codigo_postal', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'bi', 'NIF','morada', 'codigo_postal', 'password1',
            'password2', 'groups')}
         ),
    )

class FuncionarioAdmin(UserAdmin):
    form = forms.FuncionarioChangeForm
    add_form = forms.FuncionarioCreationForm
    search_fields = ('nome', 'NIF')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'bi', 'NIF','morada', 'codigo_postal', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'bi', 'NIF','morada', 'codigo_postal', 'password1',
            'password2', 'groups')}
         ),
    )

class EnfermeiroAdmin(UserAdmin):
    add_form = forms.EnfermeiroCreationForm
    search_fields = ('nome', 'NIF','especialidade')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'bi', 'NIF','morada', 'codigo_postal','especialidade', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'bi', 'NIF','morada', 'codigo_postal', 'especialidade', 'password1',
            'password2', 'groups')}
         ),
    )

class MedicoAdmin(UserAdmin):
    add_form = forms.MedicoCreationForm
    search_fields = ('nome', 'NIF','especialidade','cedula')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'bi', 'NIF','morada', 'codigo_postal','especialidade','cedula', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'bi', 'NIF','morada', 'codigo_postal', 'especialidade','cedula', 'password1',
            'password2', 'groups')}
         ),
    )

class FarmaceuticoAdmin(UserAdmin):
    add_form = forms.FarmaceuticoCreationForm
    search_fields = ('nome', 'NIF')
    ordering = ('nome',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('nome', 'bi', 'NIF','morada', 'codigo_postal','groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'nome', 'bi', 'NIF','morada', 'codigo_postal', 'password1',
            'password2', 'groups')}
         ),
    )

@admin.register(Ato_Medico)
class AtoMedicoAdmin(admin.ModelAdmin):
    list_display = ['medico', 'utente', 'hora', 'quant_med', 'medicamento',
                    'quant_art', 'outro_artigo']
    search_fields = ('medico', 'utente')
    ordering = ('utente',)

@admin.register(Ato_Enfermagem)
class AtoEnfermagemAdmin(admin.ModelAdmin):
    list_display = ['enfermeiro', 'utente', 'hora',
                    'quant_art', 'outro_artigo']
    search_fields = ('enfermeiro', 'utente')
    ordering = ('utente',)


@admin.register(Ato_Farmaceutico)
class AtoFarmaceuticoAdmin(admin.ModelAdmin):
    list_display = ['farmaceutico', 'hora', 'quant_med', 'medicamento',
                    'quant_art', 'outro_artigo']
    search_fields = ('farmaceutico',)
    ordering = ('farmaceutico',)


@admin.register(Stock_med)
class Stock_medAdmin(admin.ModelAdmin):
    list_display = ['farmaco','quant']
    search_fields = ('farmaco',)
    ordering = ('quant',)

@admin.register(Stock_art)
class Stock_artAdmin(admin.ModelAdmin):
    list_display = ['artigo','quant']
    search_fields = ('artigo',)
    ordering = ('quant',)


admin.site.register(Utente, UtenteAdmin)
admin.site.register(Enfermeiro, EnfermeiroAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Farmaceutico, FarmaceuticoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)

