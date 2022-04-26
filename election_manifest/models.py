from django.db import models

# Create your models here.
class ElectionManifest(models.Model):
    m_id = models.AutoField(primary_key=True)
    e_id = models.IntegerField()
    manifest = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'election_manifest'
