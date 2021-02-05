from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
# MY_CHOICES = (('item_key1', 'Item title 1.1'),
#               ('item_key2', 'Item title 1.2'),
#               ('item_key3', 'Item title 1.3'),
#               ('item_key4', 'Item title 1.4'),
#               ('item_key5', 'Item title 1.5'))

def get_upload_path(instance,filename):
    return 'document/{0}/{1}'.format(instance.user.username,filename)
# Create your models here.

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.FileField(upload_to = get_upload_path,blank=True)
    first_name = models.CharField(max_length=50, default='')
    middle_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=20,default='1999-12-31')

    email = models.EmailField(default='none@email.com')
    Address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    Postal_Zip_Code = models.IntegerField(default='123')
    Phone_Number = models.IntegerField(default='123')


#Qualifications:
    ssc_school=models.CharField(max_length=100, default='')
    ssc_year_of_passing=models.IntegerField( default='0')
    ssc_percentage=models.FloatField(default='100')

    hsc_school=models.CharField(max_length=100, default='')
    hsc_year_of_passing=models.IntegerField( default='0')
    hsc_percentage=models.FloatField(default='100')


    #UG
    ug_college=models.CharField(max_length=100, default='')
    ug_collage_cgpa=models.FloatField(default='100')
    ug_degree=models.CharField(max_length=100, default='')

    #PG
    pg_college = models.CharField(max_length=100, default='')
    pg_collage_cgpa = models.FloatField(default='100')
    pg_degree=models.CharField(max_length=100, default='')


    # skills = MultiSelectField(choices=MY_CHOICES)
    skills=models.CharField(max_length=100)
    any_other_qualification=models.CharField(max_length=200,default='')
    internship_experience = models.CharField(max_length=200, default='')

    certificates = models.FileField(upload_to=get_upload_path,default = 'no-img.jpg', blank=True)

    about_you = models.FileField(upload_to=get_upload_path, blank=True)

    Github=models.URLField(max_length=200, default='')
    linkedin=models.URLField(max_length=200, default='')
    facebook=models.URLField(max_length=200, default='')


    def __str__(self):
        return self.user.username




def create_resume(sender, **kwargs):
    if kwargs['created']:
        profile = Resume.objects.create(user=kwargs['instance'])

post_save.connect(create_resume, sender=User)


class ContactUs(models.Model):
    username=models.CharField(max_length=100, default="")
    From=models.EmailField(max_length=100, default="")
    Subject=models.CharField(max_length=100, default="")
    Message=models.CharField(max_length=1000, default="")


    def __str__(self):
        return self.username


class Company(models.Model):
    company_name=models.CharField(max_length=500, default="")
    location=models.CharField(max_length=500, default="")
    job_title=models.CharField(max_length=100, default="")


    def __str__(self):
        return self.company_name

