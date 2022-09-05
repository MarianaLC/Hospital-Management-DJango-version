from django.urls import path, include
from . import views


app_name = 'hospital'
urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),


    path('menuutente', views.menu_utente, name='menuutente'),
    path('menuutente/fichautente', views.ver_ficha_utente, name='fichautente'),

    path('menumedico', views.menu_medico, name='menumedico'),
    path('menumedico/infomedico', views.info_medico, name='infomedico'),
    path('menumedico/medicoatos', views.medico_atos, name='medicoatos'),
    path('menumedico/atomedico_create', views.atomedico_create, name='atomedico_create'),
    path('menumedico/atomedico_create/sucesso', views.atomedico_create, name='atomedico_create'),

    path('menuenfermeiro', views.menu_enfermeiro, name='menuenfermeiro'),
    path('menuenfermeiro/atoenfermagem_create', views.atoenfermagem_create,name='atoenfermagem_create'),
    path('menuenfermeiro/enfermeiro_info', views.info_enfermeiro,name='info_enfermeiro'),
    path('menuenfermeiro/enfermeiroatos', views.enfermeiro_atos, name='enfermeiroatos'),

    path('menufarmaceutico', views.menu_farmaceutico, name='menufarmaceutico'),
    path('menufarmaceutico/atofarmaceutico_create', views.atofarmaceutico_create,name='atofarmaceutico_create'),
    path('menufarmaceutico/info_farmaceutico', views.info_farmaceutico,name='info_farmaceutico'),
    path('menufarmaceutico/adiciona_medicamento', views.adiciona_medicamento,name='adiciona_medicamento'),
    path('menufarmaceutico/adiciona_outro_artigo', views.adiciona_outro_artigo,name='adiciona_outro_artigo'),
    path('menufarmaceutico/farmaceuticoatos', views.farmaceutico_atos, name='farmaceuticoatos'),
    path('menufarmaceutico/farmaceuticoalerta', views.farmaceutico_alerta, name='farmaceuticoalerta'),
    path('menufarmaceutico/farmaceuticostockmed', views.farmaceutico_stock_med, name='farmaceuticostockmed'),
    path('menufarmaceutico/farmaceuticostockart', views.farmaceutico_stock_art, name='farmaceuticostockart'),

    path('menufuncionario', views.menu_funcionario, name='menufuncionario'),
    path('menufuncionario/medicoestatisticas', views.medico_estatisticas, name='medicoestatisticas'),
    path('menufuncionario/enfermeiroestatisticas', views.enfermeiro_estatisticas, name='enfermeiroestatisticas'),
    path('menufuncionario/farmaceuticoestatisticas', views.farmaceutico_estatisticas, name='farmaceuticoestatisticas'),
    path('menufuncionario/utenteestatisticas', views.utente_estatisticas, name='utenteestatisticas'),
]
