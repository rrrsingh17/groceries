from django.db import models
from django.utils.translation import gettext_lazy as _

from .user import User


class Customer(User):
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    gender = models.CharField(max_length=1, choices=boolChoice)
    is_blocked = models.BooleanField('Active or Not', default=False)
    rating = models.FloatField('Rating', default=5)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    @classmethod
    def create(cls, email, password, first_name, last_name, gender, rating,
               is_blocked, is_staff=False, is_superuser=False):
        user = cls.objects.create_user(
            first_name=first_name.lower() if first_name else '',
            last_name=last_name.lower() if last_name else '',
            email=email.lower(),
            username=email.lower(),
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            gender=gender,
            is_blocked=is_blocked,
            rating=rating
        )
        return user
