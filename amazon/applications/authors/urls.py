from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='user-signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('<str:username>/profile/', views.UserProfileView.as_view(), name='profile')
]