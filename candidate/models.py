from django.db import models

# Create your models here.
class Candidate(models.Model):
    c_id = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'candidate'
