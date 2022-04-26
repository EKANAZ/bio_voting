from django.db import models

# Create your models here.
class Votting(models.Model):
    v_id = models.AutoField(primary_key=True)
    cand = models.CharField(max_length=30)
    votter = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'votting'
