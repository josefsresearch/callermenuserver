from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=64, unique=True)
    number = models.CharField(max_length=16, unique=True)
    type = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Option(models.Model):
    menu = models.ForeignKey(Menu)
    num = models.CharField(max_length=16)
    level = models.IntegerField()
    tag = models.CharField(max_length=1)
    lag = models.IntegerField(default=0)
    name = models.CharField(max_length=32)
    one = models.CharField(max_length=32,default='None')
    two = models.CharField(max_length=32,default='None')
    three = models.CharField(max_length=32,default='None')
    four = models.CharField(max_length=32,default='None')
    five = models.CharField(max_length=32,default='None')
    six = models.CharField(max_length=32,default='None')
    seven = models.CharField(max_length=32,default='None')
    eight = models.CharField(max_length=32,default='None')
    nine = models.CharField(max_length=32,default='None')
    star = models.CharField(max_length=32,default='None')
    zero = models.CharField(max_length=32,default='None')
    hash = models.CharField(max_length=32,default='None')
    question = models.CharField(max_length=32,default='None')
    website = models.CharField(max_length=32,default='None')
    phone = models.CharField(max_length=32,default='None')
    xtra = models.CharField(max_length=32,default='None')
    def __unicode__(self):
        return self.menu.name+', L='+self.num+', '+self.name
    
class User(models.Model):
    number = models.CharField(max_length=16, unique=True)
    def get_number(self):
        return self.number
    def __unicode__(self):
        return self.number
