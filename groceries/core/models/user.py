import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    phone = models.CharField(
        _('phone number'),
        max_length=15,
        default='',
        validators=[RegexValidator(PHONE_REGEX, message='Invalid phone number', code='invalid_phone')]
    )
    updated_on = models.DateTimeField(auto_now=True)

