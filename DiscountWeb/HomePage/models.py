from django.db import models

class User(models.Model):


    name = models.CharField(max_length=128,unique=True)
    ID = models.IntegerField(default=0)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    #Gender = models.CharField(max_length=32,choices=gender,default='male')


    def __str__(self):
        return self.name

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + self.code

    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'