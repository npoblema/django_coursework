from django.urls import path
from . import views  # Правильный импорт из текущего приложения

app_name = 'users'
urlpatterns = [
    path('', views.UserHomeView.as_view(), name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]
