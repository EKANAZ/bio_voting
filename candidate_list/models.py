from django.db import models
from nomination.models import Nomni
# Create your models here.

class CandidateList(models.Model):
    cl_id = models.AutoField(primary_key=True)
    # n_id = models.IntegerField()
    n=models.ForeignKey(Nomni,to_field='n_id',on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    candidate_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'candidate_list'
