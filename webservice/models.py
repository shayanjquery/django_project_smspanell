from django.db import models

# Create your models here.


class Message(models.Model):
    Phone = models.CharField(max_length=200)
    Context = models.CharField(max_length=200)
    Service = models.CharField(max_length=200)

    def __str__(self):
        return self.Phone


from django.db import models

# Create your models here.
