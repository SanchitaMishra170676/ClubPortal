from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

""" Model for PublicProfile """
class PublicProfile(models.Model):
    gender_choices  = (
        ('male','male'),
        ('female','female'),
        ('rather not say','rather not say')
        )   
   
    user            = models.OneToOneField(to=User,default= None, on_delete= models.CASCADE)
    Name            = models.CharField(max_length=150)
    Dob             = models.DateTimeField(auto_now_add=True)
    city            = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    email           = models.EmailField(max_length=255)
    phone           = models.CharField(max_length=20, blank=True)
    shortBio        = models.TextField(max_length=500,blank=True)



""" Model for resume """
class Resume(models.Model):
    user            = models.OneToOneField(to=User,default= None, on_delete= models.CASCADE)
    firstName       = models.CharField(max_length=150)
    lastName        = models.CharField(max_length=150)
    bio             = models.TextField(max_length=500,blank=True)
    email           = models.EmailField(max_length=255)
    otherInfo1      = models.CharField(max_length=300,blank=True)
    otherInfo2      = models.CharField(max_length=300,blank=True)
    facebookURL     = models.CharField(max_length=150,blank=True)
    twitterURL      = models.CharField(max_length=150,blank=True)
    instagramURL    = models.CharField(max_length=150,blank=True)
    linkedinURL     = models.CharField(max_length=150,blank=True)
    skypeURL        = models.CharField(max_length=150,blank=True)
    githubURL       = models.CharField(max_length=150,blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstName +" " +self.lastName

""" Model for achievements """
class Achievement(models.Model):
    category_choices  =( 
        ('Technical','Technical'),
        ('Non-Technical','Non-Technical'),
        ('Others','Others'),
        ('Academics','Academics')
        )    
    user                = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    achievementName     = models.CharField(max_length=255)
    category            = models.CharField(max_length=100,choices= category_choices)
    role                = models.CharField(max_length=150)
    description         = models.TextField()
    certiURL            = models.CharField(max_length=150,blank=True)
    image               = models.ImageField(upload_to="media/Dashboard/achievement/",blank=True,default="") 
    date                = models.DateTimeField(auto_now_add=True)
    is_public           = models.BooleanField(default=False)

    def __str__(self):
        return self.achievementName 

""" Model for projects """
class Project(models.Model):
    user            = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    projectName     = models.CharField(max_length=30)
    category        = models.CharField(max_length=30)
    techUsed        = models.CharField(max_length=100)
    description     = models.TextField()
    teamMembers     = models.CharField(max_length=100)
    videoURL        = models.CharField(max_length=100,blank=True)
    githubURL       = models.CharField(max_length=100)
    yourRole        = models.CharField(max_length=100,blank=True)
    time            = models.CharField(max_length=100,blank=True)
    image           = models.ImageField(upload_to="media/Dashboard/project/",default="",blank=True)   
    date            = models.DateTimeField(auto_now_add=True)
    is_public       = models.BooleanField(default=False)  

    def __str__(self):
        return self.projectName 

""" Model for hackathons """
class Hackathon(models.Model):
    achievement_choices = (
        ('first','first'),
        ('second','second'),
        ('top 5 ','top 5'),
        ('participation','participation'),
        ('others','others'))
    user                = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    hackathonName       = models.CharField(max_length=150)
    achievement         = models.CharField(max_length=150, choices=achievement_choices)
    prize               = models.CharField(max_length=250,blank=True)
    certificate         = models.CharField(max_length=200,blank=True)
    teamMembers         = models.CharField(max_length=300,blank=True)
    teamName            = models.CharField(max_length=200,blank=True)
    techStack           = models.CharField(max_length=100,blank=True)
    yourRole            = models.CharField(max_length=200,blank=True)
    description         = models.TextField()
    image               = models.ImageField(upload_to="media/Dashboard/hackathon/",default="",blank=True)
    date                = models.DateTimeField(auto_now_add=True)
    is_public           = models.BooleanField(default=False)    

    def __str__(self):
        return self.hackathonName 

""" Model for articles """
class Article(models.Model):
    user                = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    title               = models.CharField(max_length=150)
    author              = models.CharField(max_length= 50, default="")
    domain              = models.CharField(max_length=100)
    highlights          = models.TextField()
    description         = models.TextField()
    content             = models.TextField()
    code                = models.TextField(blank=True)
    subHeading          = models.CharField(max_length=200,blank=True)
    quote               = models.CharField(max_length=150,blank=True)
    quoteBy             = models.CharField(max_length=150,blank=True)
    tag1                = models.CharField(max_length=100,blank=True)
    tag2                = models.CharField(max_length=100,blank=True)
    tag3                = models.CharField(max_length=100,blank=True)
    Thumbimage1         = models.ImageField(upload_to="media/Dashboard/article/",default="",blank=True)
    Thumbimage2         = models.ImageField(upload_to="media/Dashboard/article/",default="",blank=True,null=True)
    date                = models.DateTimeField(default=timezone.now)
    is_approved         = models.BooleanField(default=False)
    slug                = models.SlugField(max_length = 200, unique=True, default="")
     
    def __str__(self):
        return self.title  

""" Model for task """
class Task(models.Model):
    user = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    taskName = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    description = models.TextField()
    resources = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.taskName 

""" Model for update """
class Update(models.Model):
    user = models.ForeignKey(to=User,default= None, on_delete= models.CASCADE)
    updateName = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.updateName 

""" Model for Resource-Courses """
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

""" Model for Resources-topic """
class Topic(models.Model):
    domain          = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name      = models.CharField(max_length=255, unique=True)
    date            = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.topic_name

""" Model for Resources-subtopic """
class SubTopic(models.Model):
    topic                = models.ForeignKey(Topic,on_delete=models.CASCADE)
    subtopic_name        = models.CharField(max_length=255, unique=True)
    image               = models.ImageField(upload_to='media/Dashboard/SubTopic/',default="", blank=True)
    date                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subtopic_name

""" Model for Resources-videolecture """
class VideoLecture(models.Model):
    subtopic             = models.ForeignKey(SubTopic,on_delete=models.CASCADE)
    title                = models.CharField(max_length=250)
    embeded_link         = models.CharField(max_length=255, unique=True)
    date                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

""" Model for Resources-PDF """
class PDF(models.Model):
    subtopic             = models.ForeignKey(SubTopic, on_delete= models.CASCADE)
    title                = models.CharField(max_length=255)
    pdf                  = models.FileField(upload_to='media/Dashboard/PDF/')
    date                 = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

""" Model for Resources-Content """
class Content(models.Model):
    subtopic            = models.ForeignKey(SubTopic, on_delete= models.CASCADE)
    title               = models.CharField(max_length=255)
    paragraph1          = models.TextField()
    paragraph2          = models.TextField(blank=True)
    code_heading        = models.CharField(max_length= 255, blank= True)
    code                = models.TextField(blank=True)
    image               = models.ImageField(blank=True, upload_to='media/Dashboard/ContentImages/')
    date                = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

""" Model for resources- other links"""
class OtherLink(models.Model):
    subtopic             = models.ForeignKey(SubTopic, on_delete= models.CASCADE)
    title                = models.CharField(max_length=255)
    description          = models.TextField(blank=True)
    link                 = models.CharField(max_length=255, unique=True)
    date                 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

""" Model for clubprofile """
class ClubProfile(models.Model):
    domain_choices = (
        ('Web Development','Web Development'),
        ('Android Development','Android Development'),
        ('IOT','IOT '),
        ('Machine Learning','Machine Learning'),        
        ('AR/VR','AR/VR')
        )
    gender_choices  = (
        ('male','male'),
        ('female','female'),
        ('rather not say','rather not say')
        )
    branch_choices = (
        ('CO','CO'),
        ('IT','IT'),
        ('CSIT','CSIT'),
        ('CSE','CSE'),
        ('EC','EC'),
        ('ME','ME'),
        ('CE','CE'),
        ('EN','EN'),
        ('other','other')
        )
    user            = models.OneToOneField(User,on_delete= models.CASCADE)
    gender          = models.CharField(max_length=50, choices =gender_choices, default="male")
    branch          = models.CharField(max_length=100, choices =branch_choices, default="CO",blank=True)
    name            = models.CharField(max_length=255)
    phone           = models.CharField(max_length=20, blank=True)
    college_email   = models.EmailField(max_length=200, unique=True)
    personal_email  = models.EmailField(max_length=200,blank=True)
    domain          = models.CharField(max_length=200, choices= domain_choices)    
    batch           = models.CharField(max_length=100,default="2020-2024")
    courses         = models.ManyToManyField(Course,blank=True)
    image           = models.ImageField(upload_to='media/dashboard/clubprofile/',blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    hostel_status   = models.CharField(max_length=255,blank=True)
    is_active       = models.BooleanField(default=True)
    is_mentor       = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) 

""" Model for announcement """
class Announcement(models.Model):    
    name = models.CharField(max_length=255)
    announcement = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

""" Models for upcoming hackathon """
class upcomingHackathon(models.Model):    
    mode_choices           = (
        ('online', 'online'),
        ('offline', 'offline')
    )
    name            = models.CharField(max_length=255)
    link            = models.CharField(max_length=255)
    mode            = models.CharField(max_length=10, choices= mode_choices, default="offline")
    description     = models.TextField(max_length=150)
    deadline        = models.DateTimeField()
    image           = models.ImageField(upload_to='media/dashboard/upcomingHackathon/',blank=True)
    is_active       = models.BooleanField(default=True)
    date            = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name