from django.db import models
from user.models import User
# Create your models here.
class Nomination(models.Model):
    n_id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    e_id = models.IntegerField()
    p_id = models.IntegerField()
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nomination'
class Nomni(models.Model):
    n_id = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,to_field='u_id',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    place = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nomni'


class Withdraw(models.Model):
    w_id = models.AutoField(primary_key=True)
    # n_id = models.IntegerField()
    withdraw_status = models.CharField(max_length=50)
    reason = models.CharField(max_length=100)
    n=models.ForeignKey(Nomni,to_field='n_id',on_delete=models.CASCADE)
    u = models.ForeignKey(User, to_field='u_id', on_delete=models.CASCADE)

    # u_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'withdraw'

