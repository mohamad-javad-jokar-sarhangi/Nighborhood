from django.db import models

class Villager(models.Model):
    name = models.CharField(max_length=255, unique=True, editable=False)
    contact_number = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=128)
    villager_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
