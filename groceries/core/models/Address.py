from django.db import models
from django.utils.translation import gettext_lazy as _

# from .customer import Customer
from .user import User


class Address(models.Model):
    customer_wise = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.CharField('House Number/Room Number', max_length=40)
    line2 = models.CharField('Block Number/Street Name', max_length=60)
    area = models.CharField('Area', max_length=40)
    city = models.CharField('City', max_length=20)
    landmark = models.CharField('Landmark', max_length=30)
    state = models.CharField('State', max_length=30)
    country = models.CharField('Country', max_length=30)
    pin_code = models.IntegerField('Pin Code')
    lon = models.FloatField('Longitude', max_length=15)
    lat = models.FloatField('latitude', max_length=15)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    @classmethod
    def create(cls, customer_wise, line1, line2, area, city, landmark, state, country):
        user = cls(
            customer_wise=customer_wise,
            line1=line1.lower() if line1 else '',
            line2=line2.lower() if line2 else '',
            area=area.lower() if area else '',
            city=city.lower() if city else '',
            landmark=landmark.lower() if landmark else '',
            state=state.lower() if state else '',
            country=country.lower() if country else '',
        )
        return user
