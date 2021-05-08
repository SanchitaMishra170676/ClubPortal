from django.contrib import admin
from .models import CodingProfile,Profile,Education,Skill


# Register your models here.
admin.site.register([Skill])

class EducationAdmin(admin.ModelAdmin):
    """ Admin Panel for Education Model """

    list_display = ('user','institution','time_period','qualification','grade')
    search_fields = ('user__user__username', 'user__user__email','institution','time_period','qualification','grade')
    list_display_links = ('user','qualification','grade')
    list_per_page= 40
    list_filter = ('qualification',)
    
    ordering = ('user',)

admin.site.register(Education, EducationAdmin)

class ProfileAdmin(admin.ModelAdmin):
    """ Admin Panel for  Profile Model """

    list_display = ('user','email','gender','dob','phone','city','state','postal_code','date')
    search_fields = ('user__user__username','user__user__email','phone','city','state')
    list_display_links = ('email','phone')
    list_per_page= 40
    list_filter = ('state','user__gender', 'user__branch', 'user__domain')
    
    ordering = ('date','email',)

admin.site.register(Profile, ProfileAdmin)


class CodingProfileAdmin(admin.ModelAdmin):
    """ Admin Panel for  CodingProfile Model """

    list_display = ('user','codechef','codeforces','spoj','leetcode','interviewbit')
    search_fields = ('user__user__username','user__user__email','codechef','codeforces','spoj','leetcode','interviewbit')
    list_display_links = ('codechef','codeforces','spoj','leetcode','interviewbit',)
    list_per_page= 40

    ordering = ('user',)

admin.site.register(CodingProfile, CodingProfileAdmin)