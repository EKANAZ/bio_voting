from django.db import models

# Create your models here.
class PostElection(models.Model):
    p_id = models.AutoField(primary_key=True)
    e_id = models.IntegerField()
    post = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'post_election'
