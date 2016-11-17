from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):

    CATEGORY = (
        ('T', 'Technology'),
        ('A', 'Arts'),
        ('TA', 'Technology and Art'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = PhoneNumberField(max_length=13)  #do a pip install django-phonenumber-field if you get errors 
    photo = models.ImageField(upload_to='profiles/', null=False)
    bio = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY)
    website = models.URLField()

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)
