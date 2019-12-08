from django.urls import path
from . import views

app_name = 'Products' 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Product_ID>/',views.detail,name='detail'),
]
