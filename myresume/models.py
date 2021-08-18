from django.db import models


class ContactResponse(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=400)
    message = models.CharField(max_length=1024)

    def __repr__(self):
        return str(self.name)
    
    __str__ = __repr__
