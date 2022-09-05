"""tp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView

from rest_framework import routers
from hospital import views

router = routers.DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet)
router.register(r'outroartigos', views.OutroArtigoViewSet)
router.register(r'utentes', views.UtenteViewSet)
router.register(r'funcionario', views.FuncionarioViewSet)
router.register(r'medicos', views.MedicoViewSet)
router.register(r'farmaceuticos', views.FarmaceuticoViewSet)
router.register(r'enfermeiros', views.EnfermeiroViewSet)
router.register(r'stock_med', views.Stock_medViewSet)
router.register(r'stock_art', views.Stock_artViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stockart/', views.Stock_artListView.as_view()),
    path('nomeart/', views.OutroArtigo_ListView.as_view()),
    path('stockmed/', views.Stock_medListView.as_view()),
    path('nomemed/', views.Medicamento_ListView.as_view()),
    path('addgroup/<int:id>/<int:gid>/', views.AddGroup),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include(router.urls)),
    path('hospital/', include('hospital.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', include('rest_framework.urls')),

]