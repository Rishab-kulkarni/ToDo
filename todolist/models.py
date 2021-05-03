from django.db import models
from django.utils.timezone import now

# Create your models here.

class TODOList(models.Model):
    addedDate = models.DateTimeField(default = now)
    text = models.CharField(default = '', max_length = 300)

    def __str__(self):
        return self.text 