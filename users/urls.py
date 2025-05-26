from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('', views.UserHomeView.as_view(), name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/', LogoutView.as_view(next_page='mailing:home'), name='logout'), 
]
