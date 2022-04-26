from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(db_column='phone number', max_length=10)  # Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    status = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    # confrim_password = models.CharField(db_column='confrim password', max_length=20)  # Field renamed to remove unsuitable characters.
    # adharcard = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
