from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .forms import CustomSignupForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('users:home')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


class CustomSignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class CustomHomeView(TemplateView):
    template_name = 'users/home.html'


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_manager()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_users_count'] = CustomUser.objects.filter(
            is_active=True).count()
        return context


@login_required
def block_user(request, user_id):
    if not request.user.is_manager():
        messages.error(request, "У вас нет прав для блокировки пользователей.")
        return redirect('mailing:home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f"Пользователь {user.email} заблокирован.")
    return redirect('users:user_list')


@login_required
def unblock_user(request, user_id):
    if not request.user.is_manager():
        messages.error(
            request,
            "У вас нет прав для разблокировки пользователей.")
        return redirect('mailing:home')
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f"Пользователь {user.email} разблокирован.")
    return redirect('users:user_list')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

from .models import CustomUser


class UserHomeView(TemplateView):
    template_name = 'users/home.html'


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserSignupView(CreateView):
    model = CustomUser
    form_class = CustomSignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
