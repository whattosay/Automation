from django.contrib import admin
from django.urls import path
from VSAAPIAnalysis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/get_response/', views.get_response, name='get_response'),
    path('api/autocomplete/', views.autocomplete, name='autocomplete'),
]