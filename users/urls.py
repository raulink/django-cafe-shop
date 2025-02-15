from django.contrib.auth.views import LoginView, LogoutView # para importar las vistas de login y logout
from django.urls import path

urlpatterns = [
    #path('register/', RegisterView.as_view(), name='register'),
    
    path(
        'login', 
        LoginView.as_view(template_name = "users/login.html"), name='login')
    #path('logout/', LogoutView.as_view(), name='logout'),
]
