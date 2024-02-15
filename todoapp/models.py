from django.db import models

# Create your models here.
class Todotype(models.Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)
    user=models.CharField(max_length=200)
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.title