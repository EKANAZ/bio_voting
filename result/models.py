from django.db import models

# Create your models here.
class Result(models.Model):
    r_id = models.AutoField(primary_key=True)
    result = models.CharField(max_length=50)
    e_id = models.IntegerField()
    c_id = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'result'

class Votting(models.Model):
    v_id = models.AutoField(primary_key=True)
    cand = models.CharField(max_length=30)
    votter = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'votting'


