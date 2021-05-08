from django.db import models
from django.utils import timezone
# Create your models here.

""" Recruitment Form Model"""
class Recruitment(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    hostel = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True)
    phone = models.CharField(max_length=10, unique=True)
    domain = models.CharField(max_length=100)
    date   = models.DateTimeField(auto_now_add=True)
    selection1 = models.BooleanField(default=False)
    selection2 =models.BooleanField(default=False)

    def __str__(self):
        return self.firstName +" " +self.lastName +"-"+ self.domain


""" Model for contact page"""
class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=800)
    subject = models.CharField(max_length=300)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    answered =models.BooleanField(default=False)
    email_subject = models.CharField(null=True , blank=True, max_length=200)
    email_body = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.email 
    

""" Model for AChievements """    
class Achievement(models.Model):
    name = models.CharField(max_length=100)
    teamName = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    prize = models.CharField(max_length=100 , blank=True)
    poster = models.ImageField(upload_to="media/Home/Achievements/",default="")
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 


""" Model for core team members """
class Core_Team_Member(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    email = models.EmailField(primary_key = True)
    linkedIn = models.CharField(max_length=255,blank=True)
    gitHub = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    coreImage= models.ImageField(upload_to="media/Home/core_team_members/",default="")
    # coreImage= models.ImageField(upload_to="core_team_members/",default="")
    date =models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


""" Model for founders """
class Founder(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(primary_key = True)
    linkedIn = models.CharField(max_length=255,blank=True)
    gitHub = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    coreImage= models.ImageField(upload_to="media/Home/Founders/",default="")

    def __str__(self):
        return self.name


""" Model for Domains """
class Domain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    domainImage= models.ImageField(upload_to="media/Home/Domain/",default="")
    
    def __str__(self):
        return self.name
    

""" Model for testimonials """   
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    Image = models.ImageField(upload_to="media/Home/Testimonials/",default="")
    position = models.CharField(max_length=150)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name +"(" +self.position+")"


""" Model for notification """
class Notification(models.Model):
    name = models.CharField(max_length=70)
    formLink = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


""" Model for Gallery Images """
class Gallery(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="media/Home/Gallery",default="")
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 
        

""" Model for updates """
class Update(models.Model):
    desc = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.desc  


""" Model for Carousel Images """
class CarouselImg(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="media/Home/CarouselImgs",default="")
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 


""" Model for developers """
class DeveloperTeam(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(primary_key = True)
    linkedIn = models.CharField(max_length=255,blank=True)
    intro = models.CharField(max_length=255, blank=True)
    image= models.ImageField(upload_to="media/Home/Developers/",default="")
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


""" Model for Volunteers """
class VolunteerTeam(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(primary_key = True)
    linkedIn = models.CharField(max_length=255,blank=True)
    intro = models.CharField(max_length=255, blank=True)
    image= models.ImageField(upload_to="media/Home/Volunteers/",default="")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name