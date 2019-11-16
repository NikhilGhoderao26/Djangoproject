from django.db import models

# Create your models here.
class djangoapp(models.Model):
    djangoapp_name = models.CharField(max_length=50)
    djangoapp_mailid = models.CharField(max_length=20)
    created_at = models.DateField()
    
    def _str_(self):
        return self.djangoapp_name

    
class Package(models.Model):
    idpackages = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, default="", null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'packages'