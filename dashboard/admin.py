from django.contrib import admin
from .models import upcomingHackathon, Resume, Achievement, Project, Hackathon, Article, Task, Update, Course, Topic, SubTopic,  VideoLecture, PDF, OtherLink, Content, ClubProfile, Announcement
from django.core.mail import send_mail,EmailMessage
from django.core import mail
from django.template.loader import render_to_string
from home.admin import send_html_mail

admin.site.register(Announcement)

# Registering models
class CourseAdmin(admin.ModelAdmin):
    """ Admin Panel for  Course Model """

    list_display = ('id','name','date')
    search_fields = ('name',)
    list_per_page= 60
    ordering = ('date',)

admin.site.register(Course,CourseAdmin)


class TopicAdmin(admin.ModelAdmin):
    """ Admin Panel for  Topic Model """

    list_display = ('id','topic_name','domain','date')
    search_fields = ('domain__name','topic_name')
    list_display_links = ('id','topic_name')
    list_per_page= 60
    list_filter = ('domain__name',)
    ordering = ('date',)

admin.site.register(Topic,TopicAdmin)


class ContentAdmin(admin.ModelAdmin):
    """ Admin Panel for  Content Model """

    list_display = ('id','subtopic','title','date')
    list_display_links = ('id','title','subtopic')
    list_per_page = 60
    search_fields = (
        'subtopic__subtopic_name','subtopic__topic__topic_name', 'subtopic__topic__domain__name',
        'title'
        )  
    list_filter = ('subtopic__topic__domain__name','subtopic__topic__topic_name')
    ordering = ('date',)

admin.site.register(Content,ContentAdmin)


class SubTopicAdmin(admin.ModelAdmin):
    """ Admin Panel for  SubTopic Model """

    list_display = ('id','topic','subtopic_name','date')
    search_fields = ('topic__topic_name','topic__domain__name','subtopic_name')
    list_display_links = ('id','subtopic_name')
    list_per_page= 60
    list_filter = ('topic__topic_name','topic__domain__name')
    ordering = ('date',)

admin.site.register(SubTopic,SubTopicAdmin)


class VideoLectureAdmin(admin.ModelAdmin):
    """ Admin Panel for  VideoLecture Model """

    list_display = ('id','subtopic','title','date')
    list_display_links = ('id','title','subtopic')
    list_per_page = 60
    search_fields = (
        'subtopic__subtopic_name','subtopic__topic__topic_name', 'subtopic__topic__domain__name',
        'title'
        )  
    list_filter = ('subtopic__topic__domain__name','subtopic__topic__topic_name')
    ordering = ('date',)

admin.site.register(VideoLecture,VideoLectureAdmin)


class PDFAdmin(admin.ModelAdmin):
    """ Admin Panel for  PDF Model """

    list_display = ('id','subtopic','title','date')
    list_display_links = ('id','title','subtopic')
    list_per_page = 60
    search_fields = (
        'subtopic__subtopic_name','subtopic__topic__topic_name', 'subtopic__topic__domain__name',
        'title'
        )  
    list_filter = ('subtopic__topic__domain__name','subtopic__topic__topic_name')
    ordering = ('date',)

admin.site.register(PDF,PDFAdmin)

class OtherLinkAdmin(admin.ModelAdmin):
    """ Admin Panel for  OtherLink Model """

    list_display = ('id','subtopic','title','date')
    list_display_links = ('id','title','subtopic')
    list_per_page = 60
    search_fields = (
        'subtopic__subtopic_name','subtopic__topic__topic_name', 'subtopic__topic__domain__name',
        'title'
        )  
    list_filter = ('subtopic__topic__domain__name','subtopic__topic__topic_name')
    ordering = ('date',)

admin.site.register(OtherLink,OtherLinkAdmin)

class ResumeAdmin(admin.ModelAdmin):
    """ Admin Panel for  Resume Model """

    list_display = ('id','user','firstName','lastName','email','date')
    search_fields = ('user__username','firstName','email')
    list_display_links = ('id','user','firstName')
    list_per_page= 60
    ordering = ('date',)

admin.site.register(Resume,ResumeAdmin)


class AchievementAdmin(admin.ModelAdmin):
    """ Admin Panel for  Achievement Model """

    list_display = ('id','user','achievementName','category','is_public','date')
    list_display_links = ('id','achievementName')
    list_per_page = 60
    search_fields = ('user__username','achievementName')  
    list_filter = ('category','is_public')
    ordering = ('date',)

admin.site.register(Achievement,AchievementAdmin)


class ProjectAdmin(admin.ModelAdmin):
    """ Admin Panel for  Project Model """

    list_display = ('id','user','projectName','category','is_public','date')
    list_display_links = ('id','projectName')
    list_per_page = 60
    search_fields = ('user__username','projectName','teamMembers')  
    list_filter = ('category','is_public')
    ordering = ('date',)

admin.site.register(Project,ProjectAdmin)


class HackathonAdmin(admin.ModelAdmin):
    """ Admin Panel for  Hackathon Model """

    list_display = ('id','user','hackathonName','achievement','teamName','is_public','date')
    list_display_links = ('id','hackathonName')
    list_per_page = 60
    search_fields = ('user__username','hackathonName','teamMembers','teamName')  
    list_filter = ('achievement','is_public')
    ordering = ('date',)

admin.site.register(Hackathon,HackathonAdmin)


class ArticleAdmin(admin.ModelAdmin):
    """ Admin Panel for  Article Model """

    list_display = ('id','user','title','domain','is_approved','date')
    list_display_links = ('id','user','title')
    list_per_page = 60
    search_fields = ('user__username','title','domain')  
    list_filter = ('domain','is_approved')
    ordering = ('date',)

admin.site.register(Article,ArticleAdmin)


class TaskAdmin(admin.ModelAdmin):
    """ Admin Panel for  Task Model """

    list_display = ('id','user','taskName','date')
    list_display_links = ('id','taskName')
    list_per_page = 60
    search_fields = ('user__username','taskName')  
    ordering = ('date',)

admin.site.register(Task,TaskAdmin)


class UpdateAdmin(admin.ModelAdmin):
    """ Admin Panel for  Update Model """

    list_display = ('id','user','updateName','date')
    list_display_links = ('id','updateName')
    list_per_page = 60
    search_fields = ('user__username','updateName')  
    ordering = ('date',)

admin.site.register(Update,UpdateAdmin)


class ClubProfileAdmin(admin.ModelAdmin):
    """ Admin Panel for  ClubProfile Model """

    list_display = ('id','user','name','branch','domain','gender','batch','is_mentor','is_active','college_email')
    list_display_links = ('id','name')
    list_per_page = 60
    search_fields = ('user__username','user__email')  
    list_filter = ('branch','domain','gender','batch','is_mentor','is_active')
    ordering = ('date',)
    actions = ['send_Activation_AccountEmail']

    def send_Activation_AccountEmail(self, request, queryset):
        connection = mail.get_connection()
        # connection.open()
        pl =[]
        connection.open()
        for i in queryset:
            
            message= render_to_string('emails/AccountActivationEmail.html',{'username': i.user.username})
            send_html_mail("Credentials For Activated Account",message,[i.user.email]) 
            i.is_active = True
            i.save()
            # # print(i.email)
            # if i.email:
            #     pl.append(i.email)
            # # else:
        connection.close()
        self.message_user(request, "Mail sent successfully ")
    send_Activation_AccountEmail.short_description = "Send Account Activation Email"



admin.site.register(ClubProfile,ClubProfileAdmin)


class upcomingHackathonAdmin(admin.ModelAdmin):
    """ Asmin Pannel for hackathons """
    list_display = ('name','mode','description','deadline','is_active')
    list_display_links = ('name','mode','description','deadline')
    list_per_page = 30
    search_fields = ('name','mode','deadline')  
    list_filter = ('mode',)
    ordering = ('deadline',)

admin.site.register(upcomingHackathon,upcomingHackathonAdmin)