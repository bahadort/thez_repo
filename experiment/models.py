from django.db import models

class Experiment(models.Model):
    image= models.ImageField(upload_to='images/')
    check_box= models.BooleanField()