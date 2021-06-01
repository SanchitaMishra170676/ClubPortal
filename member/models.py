from django.db import models
from django.contrib.auth.models import User
from dashboard.models import ClubProfile
import random
# Create your models here.

""" Function to get random string """
def getRandomString():
    return str(random.randbytes(64))

""" Model for coding profiles of users """
class CodingProfile(models.Model):
    user = models.OneToOneField(ClubProfile,on_delete=models.CASCADE)
    codechef = models.CharField(max_length=255,default='N/A',blank=True)
    codeforces = models.CharField(max_length=255,default='N/A',blank=True)
    spoj = models.CharField(max_length=255,default='N/A',blank=True)
    leetcode = models.CharField(max_length=255,default='N/A',blank=True)
    gfg = models.CharField(max_length=255,default='N/A',blank=True)
    codechef_questions = models.CharField(max_length=255,default='0')
    codeforces_questions = models.CharField(max_length=255, default='0')
    spoj_questions = models.CharField(max_length=255, default='0')
    leetcode_questions = models.CharField(max_length=255, default='0')
    gfg_questions = models.CharField(max_length=255, default='0')


    def __str__(self):
        return self.user.user.username


""" Model for profiles of users"""
class Profile(models.Model):
    gender_choices = (
        ('male','male'),
        ('female','female'),
        ('other', 'other')
    )
    user=  models.OneToOneField(ClubProfile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255,default='male')    
    phone = models.CharField(max_length=15,blank=True)
    dob = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255,blank=True)
    state = models.CharField(max_length=255,blank=True)
    postal_code = models.IntegerField(default=123456)
    email = models.EmailField(max_length=255,blank=True)
    short_bio   = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    username = models.SlugField(max_length = 200, unique=True, default=getRandomString)
    def __str__(self):
        return self.user.user.username


""" Model for Education of users """
class Education(models.Model):
    user = models.ForeignKey(ClubProfile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=400)
    time_period = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.user.user.username


""" Model for Skills of users"""
class Skill(models.Model):
    user = models.ForeignKey(to=ClubProfile, on_delete= models.CASCADE)
    skill = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.user.username



    

