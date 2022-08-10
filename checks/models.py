from django.db import models

# Create your models here.
class Blacklist(models.Model):
    md5 = models.CharField(unique=True, max_length=45)
    sha256 = models.CharField(unique=True, max_length=65)
    cert_sha1 = models.CharField(max_length=45)
    packagename = models.CharField(max_length=300)
    

    class Meta:
        managed = False
        db_table = 'blacklist'

class Whitelist(models.Model):
    md5 = models.CharField(unique=True, max_length=45)
    sha256 = models.CharField(max_length=65)
    cert_sha1 = models.CharField(max_length=45)
    packagename = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'whitelist'
