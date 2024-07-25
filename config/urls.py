from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aplicacionN1/', include("aplicacionN1.urls"))
]