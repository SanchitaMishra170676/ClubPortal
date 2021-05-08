from django.shortcuts import render, redirect 
from django.contrib import messages
from .models import Founder,Gallery,VolunteerTeam, DeveloperTeam, Update,CarouselImg, Core_Team_Member as CoreMember,Domain , Notification, Testimonial,Contact,Achievement, Recruitment
from dashboard.models import (ClubProfile, Article)
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.core import mail
from member.models import (CodingProfile, Education, Skill)
from dashboard.models import (Hackathon, Achievement as UserAchievement, Project, Article, Announcement)
# from .codingScore import UserData
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


""" Function for home page """
def home(request):
# Member View
    if request.user.is_authenticated:
        clubProfile = {}
        educationProfile = {}
        codingProfile = {}
        codingSolved = {}
        codingRating = {}
        
        #statistics
        blogs = {}
        projects ={}
        hackathons = {}
        achievements = {}
        stats ={}

        stats['private_achievements'] = UserAchievement.objects.filter(is_public=False,user=request.user).count()
        stats['total_achievements'] = UserAchievement.objects.filter(user=request.user).count()
        stats['public_achievements'] = stats['total_achievements'] - stats['private_achievements']


        stats['private_projects'] = Project.objects.filter(is_public=False,user=request.user).count()
        stats['total_projects'] = Project.objects.filter(user=request.user).count()
        stats['public_projects'] = stats['total_projects'] - stats['private_projects']


        stats['private_hackathons'] = Hackathon.objects.filter(is_public=False,user=request.user).count()
        stats['total_hackathons'] = Hackathon.objects.filter(user=request.user).count()
        stats['public_hackathons'] = stats['total_hackathons'] - stats['private_hackathons']
      
        # for skills
        skills = {}

        announcements = Announcement.objects.order_by('-date').all()
        try: 
            request.session['clubprofile'] = [ i.name for i in ClubProfile.objects.get(user=request.user).courses.all()]
            clubProfile = ClubProfile.objects.get(user=request.user)
            try:    
                #statistics
                blogs = Article.objects.filter(user=request.user)
                projects = Project.objects.filter(user=request.user)
                hackathons = Hackathon.objects.filter(user=request.user)
                achievements = UserAchievement.objects.filter(user=request.user)
                # print(projects)
                #profile
                codingProfile = CodingProfile.objects.get(user=clubProfile)
                educationProfile = Education.objects.filter(user = clubProfile)
                #skills
                skills = Skill.objects.filter(user=clubProfile)

                # if codingProfile:
                #     if(codingProfile.codechef):
                #         codingSolved['codechef'] =  UserData(codingProfile.codechef).get_details('codechef')['fsolved']
                #         codingRating['codechef'] = UserData(codingProfile.codechef).get_details('codechef')['rating']
                #     else:
                #         codingSolved['codechef'] = 'N/A'
                #         codingRating['codechef']  = 'N/A'
                #     if(codingProfile.codeforces):
                #         codingSolved['codeforces'] =  UserData(codingProfile.codeforces).get_details('codeforces')['solved']
                #         codingRating['codeforces'] = UserData(codingProfile.codeforces).get_details('codeforces')['rating']
                #     else:
                #         codingSolved['codeforces'] = 'N/A'
                #         codingRating['codeforces']  = 'N/A'
            except:
                pass           
        except:
            request.session['clubprofile'] = []
        # print(hackathons[0].teamName)
        context ={
            'clubProfile':clubProfile, 
            'codingProfile':codingProfile,
            'codingSolved':codingSolved,
            'codingRating':codingRating,'educationProfiles':educationProfile, 
            'stats': stats,
            'projects':projects,
            'blogs':blogs,
            'achievements': achievements,
            'hackathons':hackathons,
            'skills': skills,
            'announcements': announcements
        }        
        return render(request,'dashboard/home.html', context)    
# Public View 
    else:
        domains = Domain.objects.all() 
        achievement = Achievement.objects.order_by('-date').filter(active=True)[:8]

        coreMember = CoreMember.objects.filter(active=True)
        founder = Founder.objects.all()
        testimonial = Testimonial.objects.filter(active=True)
        notification = Notification.objects.filter(active=True)
        update = Update.objects.filter(active = True)
        carouselImg = CarouselImg.objects.filter(active=True)
        context = {'carouselImgs': carouselImg,'founders':founder,'updates': update, 'achievements':achievement, 'coreMembers':coreMember,'domains':domains, 'notifications':notification,'testimonials':testimonial}
        return render(request, 'home/index.html',context)


""" Function for contact page """
def contact(request):
    if request.user.is_authenticated:
        return redirect('404_not_found')
    if request.method =='POST':
        Name = request.POST.get('name')  
        Message = request.POST.get('message')
        Subject = request.POST.get('subject') 
        Email = request.POST.get('email')
        contact = Contact(name=Name, message=Message, subject=Subject, email=Email)
        contact.save()
        messages.success(request,'Querry Received! will contact you soon.')
        return redirect ('contact')
    update = Update.objects.filter(active = True)
    context = {'updates': update}    
    return render(request, 'home/contact.html', context)


""" Function for achievement page """
def achievement(request):
    if request.user.is_authenticated:
        return redirect('404_not_found')
    achievement = Achievement.objects.order_by('-date').filter(active=True)
    update = Update.objects.filter(active = True)
        # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(achievement,8)
    try:
        achievements = paginator.page(page)
    except PageNotAnInteger:   
        achievements = paginator.page(1)
    except EmptyPage:
        achievements = paginator.page(paginator.num_pages)

    context = {'achievements':achievements,'updates': update}
    return render(request, 'home/achievements.html', context)


""" Function for Recruitment Page """
def recruitment(request):
    if request.user.is_authenticated:
        return redirect('404_not_found')
    if request.method == "POST":
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Gender = request.POST['Gender']
        Branch = request.POST['Branch']
        # Section = request.POST['Section']
        HostelName = request.POST['HostelName']
        Email = request.POST['Email']
        PhoneNo = request.POST['PhoneNo']
        Domain = request.POST['Domain']
        PriorKnowledge = request.POST['PriorKnowledge']
        recr = Recruitment.objects.filter(email=Email)
        recr2 = Recruitment.objects.filter(phone = PhoneNo)
        if (len(recr) or len(recr2)):
            messages.error(request,"This entry already exists.")
            return redirect ('recruitment')
        else:
            ins = Recruitment(firstName = FirstName, lastName= LastName, gender= Gender, branch=Branch, hostel=HostelName, email=Email, phone=PhoneNo, domain= Domain )
            # ins.save()                     
            messages.success(request,'Registration Successful!, The credentials are sent to your college id')
            connection = mail.get_connection()
            connection.open()
            message= render_to_string('emails/emailTemplate.html',{})
            email_ver =  EmailMessage(
            "Registration Successful!",
            message
            ,to=[Email])    
            ins.save()
        # email_ver.fail_silently=False,
            email_ver.content_subtype = 'html'
            email_ver.send()
            connection.close()
            return redirect ('recruitment')            
    return render(request, 'home/rec-form.html')


""" Function for Gallery """
def gallery(request):
    if request.user.is_authenticated:
        return redirect('404_not_found')
    gallery = Gallery.objects.filter(active=True) 
    # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(gallery,15)
    try:
        gallerys = paginator.page(page)
    except PageNotAnInteger:   
        gallerys = paginator.page(1)
    except EmptyPage:
        gallerys = paginator.page(paginator.num_pages)

    context = {'gallerys':gallerys}   
    return render(request, 'home/gallery.html', context)


""" Function for developer's page """
def team(request): 
    if request.user.is_authenticated:
        return redirect('404_not_found')
    developers = DeveloperTeam.objects.filter(active=True)
    volunteers = VolunteerTeam.objects.filter(active=True)
    context = {'developers': developers, 'volunteers': volunteers}
    return render(request, 'home/team.html',context)    


""" Function for Article/ Blog """
def blog(request,the_slug):
    try:
        articles = Article.objects.order_by('-date').filter(is_approved=True)[:7]
        webCnt= Article.objects.filter(is_approved=True,domain='Web_Development').count()
        androidCnt = Article.objects.filter(is_approved=True,domain='Android_Development').count()
        mlCnt = Article.objects.filter(is_approved=True,domain='Machine_Learning').count()
        iotCnt = Article.objects.filter(is_approved=True,domain='Internet_Of_Things').count()
        xrCnt= Article.objects.filter(is_approved=True,domain='AR_VR').count()
        try:
            article = Article.objects.get(slug=the_slug)
        except:
            message.error("Invalid URL")
        context = {'article':article, 'articles': articles,'webCnt':webCnt,'androidCnt':androidCnt,'mlCnt':mlCnt,'iotCnt':iotCnt,'xrCnt':xrCnt}
        return render(request,'dashboard/articles/blog.html',context)
    except:
        return redirect('404_not_found')


""" Function for listing all articles """
def blog_list(request):
    try:
        article = Article.objects.order_by('-date').filter(is_approved=True)
        # Pagination
        page = request.GET.get('page',1)
        paginator = Paginator(article,6)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:   
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        latestarticles = article[:7]
        webCnt= Article.objects.filter(is_approved=True,domain='Web_Development').count()
        androidCnt = Article.objects.filter(is_approved=True,domain='Android_Development').count()
        mlCnt = Article.objects.filter(is_approved=True,domain='Machine_Learning').count()
        iotCnt = Article.objects.filter(is_approved=True,domain='Internet_Of_Things').count()
        xrCnt= Article.objects.filter(is_approved=True,domain='AR_VR').count()
        context = {'articles': articles,'latestarticles':latestarticles, 'webCnt':webCnt,'androidCnt':androidCnt,'mlCnt':mlCnt,'iotCnt':iotCnt,'xrCnt':xrCnt}
        return render(request,'dashboard/articles/blog_list.html',context)
    except:
        return redirect('404_not_found')


""" Function for listing articles as per the category """
def blog_list_category(request,category):
    try:
        article = Article.objects.order_by('-date').filter(is_approved=True,domain=category)
        # Pagination 
        page = request.GET.get('page',1)
        paginator = Paginator(article,6)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:   
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        latestarticles = article[:7]
        webCnt= Article.objects.filter(is_approved=True,domain='Web_Development').count()
        androidCnt = Article.objects.filter(is_approved=True,domain='Android_Development').count()
        mlCnt = Article.objects.filter(is_approved=True,domain='Machine_Learning').count()
        iotCnt = Article.objects.filter(is_approved=True,domain='Internet_Of_Things').count()
        xrCnt= Article.objects.filter(is_approved=True,domain='AR_VR').count()
        context = {'articles': articles,'latestarticles':latestarticles, 'webCnt':webCnt,'androidCnt':androidCnt,'mlCnt':mlCnt,'iotCnt':iotCnt,'xrCnt':xrCnt}
        return render(request,'dashboard/articles/blog_list.html',context)
    except:
        return redirect('404_not_found')



# def custom_page_not_found_view(request, exception=None):
#     return render(request, "error/404.html")

# def custom_error_view(request, exception=None):
#     return render(request, "error/500.html")

# def custom_permission_denied_view(request, exception=None):
#     return render(request, "error/403.html")

# def custom_bad_request_view(request, exception=None):
#     return render(request, "error/400.html")
