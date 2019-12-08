from django.urls import path
 
from . import views
 
app_name = 'HomePage' 
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('comfirm/',views.user_confirm),
    path('logout/',views.logout),
    #path('captcha',include('captcha.urls')),
]
