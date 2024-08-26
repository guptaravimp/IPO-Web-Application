from django.db import models
# from django.db import models
# class Teacher(models.Model):
#     name = models.CharField(max_length=80)
#     age = models.IntegerField()
# Create your models here.
class IPOUpcoming(models.Model):
    icons=models.FileField(upload_to='home/')
    company_name=models.CharField(max_length=100)
    company_link=models.URLField(max_length=200)
    price_band=models.CharField( max_length=50)
    open_date=models.DateField(auto_now_add=True)
    close_date=models.DateField(auto_now_add=True)
    issue_size=models.CharField(max_length=50)
    issue_type=models.CharField(max_length=50)
    listing_date=models.DateField(auto_now_add=True)

class FaqModel(models.Model):
    question=models.CharField(max_length=200)
    ans1=models.CharField(max_length=300)
    ans2=models.CharField(max_length=300)
    ans3=models.CharField(max_length=300)
    ans4=models.CharField(max_length=300)
    ans5=models.CharField(max_length=300)




