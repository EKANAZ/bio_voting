from django.db import models

# Create your models here.

class Election(models.Model):
    e_id = models.AutoField(primary_key=True)
    election = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'election'
