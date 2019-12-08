from django.db import models

class User(models.Model):
    gender = (
        ('male','female'),
        )

    Name = models.CharField(max_length=128,unique=True)
    ID = models.IntegerField(default=0)
    Password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    Gender = models.CharField(max_length=32,choices=gender,default='male')


    def __str__(self):
        return self.name