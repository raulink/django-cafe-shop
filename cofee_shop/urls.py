"""
URL configuration for cofee_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from django.conf import settings    #para que se pueda ver las imagenes en el panel de administración
from django.conf.urls.static import static  #para que se pueda ver las imagenes en el panel de administración

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls')),
    path('usuarios/', include('users.urls')), # Se tiene que añadir el nombre de la app creada antes de realizar las migraciones e inclusion a la base de datos
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para que se pueda ver las imagenes en el panel de administración

