from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/energie-solaire/', views.service_solaire, name='service_solaire'),
    path('services/videosurveillance/', views.service_videosurveillance, name='service_videosurveillance'),
    path('services/controle-acces/', views.service_controle_acces, name='service_controle_acces'),
    path('services/electricite-generale/', views.service_electricite, name='service_electricite'),
    path('services/reseau-informatique/', views.service_reseau, name='service_reseau'),
    path('services/telephonie/', views.service_telephonie, name='service_telephonie'),
    path('services/securite-incendie/', views.service_incendie, name='service_incendie'),
    path('services/cloture-electrique/', views.service_cloture, name='service_cloture'),
    path('services/maintenance/', views.service_maintenance, name='service_maintenance'),
    path('demande-devis/', views.demande_devis, name='demande_devis'),
]


