from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    category_id=models.AutoField(primary_key=True,unique=True)
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Spend(models.Model):
    
    spend_id=models.AutoField(primary_key=True,unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0,validators=[MinValueValidator(0)])
    date_added=models.DateField()
    comments=models.CharField(max_length=400,null=True)

    def __str__(self):
        return str(self.amount)


