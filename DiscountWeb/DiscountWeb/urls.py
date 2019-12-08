from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('HomePage/', include('HomePage.urls')),
    path('Products/', include('Products.urls')),
    path('admin/', admin.site.urls),
]

