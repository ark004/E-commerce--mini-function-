from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class catg(models.Model):
    name=models.CharField(max_length=120,unique=True)
    slug=models.SlugField(max_length=120,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('prod_ct',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class prod(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name=models.CharField(max_length=120,unique=True)
    slug=models.SlugField(max_length=120,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(catg,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])


