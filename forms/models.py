from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.date}"
    def __str__(self):
        return self.get_full_name()
