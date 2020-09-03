from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    line1 = models.CharField(max_length=256)
    line2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=2,
        validators=[RegexValidator(r'^([a-zA-Z]){2}$',
                        'State must be 2 letters. Example, "CA".')])
    zipcode = models.CharField(max_length=5,
        validators=[RegexValidator(r'^\d{5}$', 'Zip code must be 5 digits.')])


    def save(self, *args, **kwargs):
        self.state = self.state.upper()
        super().save(*args, **kwargs)
