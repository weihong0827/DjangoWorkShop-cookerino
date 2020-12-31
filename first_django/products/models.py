from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10000)

    def __str__(self):
        return '{}{}'.format(self.title,self.price)
    @classmethod
    def _delete_data(cls):
        Product.objects.all().delete()
    
    @classmethod
    def _create_data(cls,count = 1000):
        for i in range (count):
            Product.objects.create(title='title'+str(i),description = 'This is the description for title'+str(i),price=i)

class seller(models.Model):
    name = models.TextField()
    age = models.IntegerField()

