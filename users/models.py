from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', _('User')),
        ('manager', _('Manager')),
    )

    email = models.EmailField(_('email address'), unique=True)
    is_email_verified = models.BooleanField(
        default=False,
        help_text=_('Indicates whether the user has verified their email address.')
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        help_text=_('Role of the user in the system.')
    )

    # Поле is_active уже есть в AbstractUser, поэтому его переопределение не требуется,
    # но если вы хотите добавить кастомное описание, можно оставить
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as active.')
    )

    USERNAME_FIELD = 'email'  # Используем email для аутентификации
    REQUIRED_FIELDS = []  # Убираем требование имени пользователя

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def is_manager(self):
        return self.role == 'manager'

    def is_user(self):
        return self.role == 'user'