from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('manager', 'Manager'),
    )
    email = models.EmailField(_('email address'), unique=True)
    is_email_verified = models.BooleanField(
        default=False)  # Флаг подтверждения email
    is_active = models.BooleanField(
        default=True)  # Для блокировки пользователей
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user')  # Роль пользователя

    USERNAME_FIELD = 'email'  # Используем email для аутентификации
    REQUIRED_FIELDS = []  # Убираем требование имени пользователя

    def __str__(self):
        return self.email

    def is_manager(self):
        return self.role == 'manager'

    def is_user(self):
        return self.role == 'user'
