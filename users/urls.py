from django.contrib.auth.views import LoginView, LogoutView # para importar las vistas de login y logout
from django.urls import path

from .views import RegisterView

urlpatterns = [
    #path('register/', RegisterView.as_view(), name='register'),
    
    path(
        'login', 
        LoginView.as_view(template_name = "users/login.html"), name='login')
    ,    
    path('registro', RegisterView.as_view(), name='registro'),
    #path('profile/', ProfileView.as_view(), name='profile'),
    #path('update/', UpdateProfileView.as_view(), name='update'),
    # path logout
    path('logout', LogoutView.as_view(), name='logout'),
    

]
