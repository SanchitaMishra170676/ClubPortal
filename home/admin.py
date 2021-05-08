from django.contrib import admin
from .models import Recruitment,DeveloperTeam, VolunteerTeam, Contact, CarouselImg,Core_Team_Member, Founder,Domain, Notification,Gallery,Testimonial, Achievement, Update
from django.core.mail import send_mail,EmailMessage
from django.core import mail
from django.template.loader import render_to_string
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

import threading
from threading import Thread

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, 'innogeeks.kiet.edu', self.recipient_list)
        msg.content_subtype = "html"
        msg.send()
        
def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


class RecruitmentAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Recruitment Model """
    list_display = ('id','email','firstName','domain','gender','phone','branch','hostel','date')
    search_fields = ('email','firstName','gender','phone','branch', 'domain','hostel')
    list_display_links = ('id','email','phone')
    list_per_page= 80
    list_filter = ('gender','domain','branch','hostel')
    ordering = ('date','email')
    actions = ['send_EMAIL','send_CORRECT_EMAIL','send_SECONDYR_EMAIL']

    def send_EMAIL(self, request, queryset):
        connection = mail.get_connection()
        # connection.open()
        pl =[]
        for i in queryset:
            print(i.email)
            if i.email:
                pl.append(i.email)
            # else:

        connection.open()
        send_html_mail('sitest','<h1>hello</h1>',pl) 

        connection.close()
        self.message_user(request, "Mail sent successfully ")
    send_EMAIL.short_description = "Send an email to selected users"

    def send_CORRECT_EMAIL(self, request, queryset):
        connection = mail.get_connection()
        # connection.open()
        pl =[]
        for i in queryset:
            # print(i.email)
            if i.email:
                pl.append(i.email)
            # else:
        # print(pl)

        connection.open()
        message= render_to_string('emails/updateEmail.html')
        send_html_mail("Reagarding your Recruitment process(update email address)",message,pl) 

        connection.close()
        self.message_user(request, "Mail sent successfully ")
    send_CORRECT_EMAIL.short_description = "Send email for correctness of email"

    def send_SECONDYR_EMAIL(self, request, queryset):
        connection = mail.get_connection()
        # connection.open()
        pl =[]
        for i in queryset:
            # print(i.email)
            if i.email:
                pl.append(i.email)
            # else:
        # print(pl)

        connection.open()
        message= render_to_string('emails/secondYrRecruitment.html')
        send_html_mail("Registration Closed for Second Year!",message,pl) 

        connection.close()
        self.message_user(request, "Mail sent successfully ")
    send_SECONDYR_EMAIL.short_description = "Send sorry email for secondyr"
admin.site.register(Recruitment, RecruitmentAdmin)

class ContactAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Queries Model """

    list_display = ('id','email','name','subject','date','answered')
    search_fields = ('email','name','subject','message','id')
    list_display_links = ('id','email','subject')
    list_filter = ('answered',)
    list_per_page= 60

    def save_model(self, request, obj, form, change):
        if obj.answered:
            connection = mail.get_connection()
            connection.open()
            message= render_to_string('emails/contactTemplate.html',{'message':obj.email_body})
            
            send_html_mail(str(obj.email_subject),message,[obj.email])
            connection.close()
            self.message_user(request, "Mail sent successfully ")
        obj.save()
                   
    ordering = ('date',)

admin.site.register(Contact,ContactAdmin)

class UpdateAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Update Model """

    list_display = ('id','desc','link','active')
    search_fields = ('active','desc','link')
    list_display_links = ('desc','link',)
    list_filter = ('active',)
    list_per_page= 30
    

    ordering = ('date',)

admin.site.register(Update,UpdateAdmin)

class AchievementAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Achievement Model """

    list_display = ('id','name','rank','prize','active','date')
    search_fields = ('active','name','rank','prize','teamName')
    list_display_links = ('name','rank',)
    list_filter = ('active',)
    list_per_page= 20
    

    ordering = ('date',)

admin.site.register(Achievement,AchievementAdmin)


class TestimonialAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Testimonial Model """

    list_display = ('id','name','position','message','active')
    search_fields = ('name','position','message','active')
    list_display_links = ('name','message',)
    list_filter = ('active',)
    list_per_page= 20
    


admin.site.register(Testimonial,TestimonialAdmin)


class GalleryAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Gallery Model """

    list_display = ('id','name','active')
    search_fields = ('name',)
    list_display_links = ('name',)
    list_filter = ('active',)
    list_per_page= 15
    

    ordering = ('date',)

admin.site.register(Gallery,GalleryAdmin)

class NotificationAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Achievement Model """

    list_display = ('id','name','formLink','active')
    search_fields = ('name',)
    list_display_links = ('name',)
    list_filter = ('active',)
    list_per_page= 20
    

    ordering = ('date',)

admin.site.register(Notification,NotificationAdmin)

class DomainAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Domain Model """

    list_display = ('id','name','description')
    search_fields = ('name','description')
    list_display_links = ('name','description')
    list_filter = ('name',)
    list_per_page= 20
    

admin.site.register(Domain,  DomainAdmin)

class FounderAdmin(ImportExportModelAdmin):
    """ Admin Panel for Founder Model """

    list_display = ('name','email')
    search_fields = ('name','email')
    list_display_links = ('name','email')
    list_per_page= 10
    

admin.site.register(Founder,FounderAdmin)



class Core_Team_MemberAdmin(ImportExportModelAdmin):
    """ Admin Panel for  Core_Team_Member Model """

    list_display = ('name','branch','year','email','active')
    search_fields = ('name','branch','year','email','active')
    list_display_links = ('name','email',)
    list_filter = ('active',)
    list_per_page= 30
    

    ordering = ('date',)

admin.site.register(Core_Team_Member,Core_Team_MemberAdmin)


class CarouselImgAdmin(ImportExportModelAdmin):
    """ Admin Panel for  CarouselImg Model """

    list_display = ('id','name','active')
    search_fields = ('name','active')
    list_display_links = ('name','active')
    list_filter = ('active',)
    list_per_page= 20


    ordering = ('date',)

admin.site.register(CarouselImg,CarouselImgAdmin)

class DeveloperTeamAdmin(ImportExportModelAdmin):
    """ Admin Panel for  DeveloperTeam Model """

    list_display = ('name','email','linkedIn','intro','active')
    search_fields = ('email','name')
    list_display_links = ('email',)
    list_per_page= 60
    list_filter = ('active',)
    

    ordering = ('name',)

admin.site.register(DeveloperTeam,DeveloperTeamAdmin)


class VolunteerTeamAdmin(ImportExportModelAdmin):
    """ Admin Panel for  VolunteerTeam Model """

    list_display = ('name','email','linkedIn','intro','active')
    search_fields = ('email','name')
    list_display_links = ('email',)
    list_per_page= 60
    list_filter = ('active',)
    

    ordering = ('name',)

admin.site.register(VolunteerTeam,VolunteerTeamAdmin)
