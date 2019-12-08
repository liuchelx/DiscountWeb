from django.db import models
 
class Product(models.Model):

    Product_ID = models.IntegerField(default=0) 
    ProductName = models.CharField(max_length=200) #product name
    PubTime = models.DateTimeField('Product Released') #product release time
    OriPrice = models.FloatField(default=0)
    DisPrice = models.FloatField(default=0)
    link = models.URLField(max_length=500)
    Tag = models.CharField(max_length=200)
    click = models.IntegerField(default=0)
    EndTime = models.DateTimeField('Discount End') #
    def __str__(self):
        return self.ProductName

 
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
