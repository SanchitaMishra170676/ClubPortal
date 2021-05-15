from django.shortcuts import render, redirect, HttpResponse
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from .models import (
    Resume, Achievement, Project, Hackathon, Article, Task, Update, Course, Topic, SubTopic,  VideoLecture, PDF, Content, OtherLink, ClubProfile, upcomingHackathon )
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from member.models import (CodingProfile,Profile, Education,Skill)
import os
from django.conf import settings

""" Function to add achievement """
@login_required
def add_achievement(request): 
    if request.method == "POST": 
        try:
            User = request.user
            AchievementName = request.POST['AchievementName']
            Category = request.POST['Category']
            Role = request.POST['Role']
            Description = request.POST['Description']
            CertiURL = request.POST['CertiURL']
            try:
                Image = request.FILES['Image']
            except:
                Image = None
            is_public = True if request.POST['is_public'] =='public' else False
            inst = Achievement(user = User, achievementName = AchievementName, category = Category, role= Role, description= Description, certiURL= CertiURL, image= Image, is_public=is_public)
            inst.save()
            messages.success(request,'Achievement Added Successfully')
            return redirect('achievement')
        except:
            messages.error(request, 'An error occurred, Contact to team')
            return redirect('add_achievement')       
    return render(request,'dashboard/achievements/add_achievement.html')


""" Function to delete achievement """
@login_required 
def delete_achievement(request,pk):
    try:
        achievement = Achievement.objects.get(pk=pk, user=request.user)
        achievement.delete()
        messages.success(request, 'An achievement was successfully deleted')
        return redirect('achievement')
    except:
        return redirect('404_not_found')
        

""" Function to update achievement """
@login_required 
def update_achievement(request,pk):
    try:
        if request.method == "POST":
            achievement = Achievement.objects.get(user=request.user, id=pk)
            achievement.achievementName = request.POST['AchievementName']
            achievement.category = request.POST['Category']
            achievement.role = request.POST['Role']
            achievement.description = request.POST['Description']
            achievement.certiURL = request.POST['CertiURL']
            try:
                achievement.image = request.FILES['Image']
            except:
                pass
            # achievement.is_public = request.POST['is_public']
            achievement.is_public = True if request.POST['is_public'] =='public' else False  
            achievement.save()
            messages.success(request,'Updated successfully')
            return redirect('achievement')          
        achievement = Achievement.objects.get(user=request.user, id=pk)
        return render(request,'dashboard/achievements/update_achievement.html',{'achievement':achievement})
    except:
        return redirect('404_not_found')


""" Function to display achievement list """

@login_required
def achievement(request):
    acmts = Achievement.objects.filter(user=request.user)
    # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(acmts,8)
    try:
        achievements = paginator.page(page)
    except PageNotAnInteger:   
        achievements = paginator.page(1)
    except EmptyPage:
        achievements = paginator.page(paginator.num_pages)
    
    context = {'achievements': achievements}
    return render(request,'dashboard/achievements/achievement.html',context)


""" Function for personal profile """

@login_required
def personal_profile(request):
    context = { 'personalProfile':{},'codingProfile':{},'educationProfiles':{},'skills':{},'clubProfile':{}}

    try:
        cpuser  = ClubProfile.objects.filter(user=request.user)
        request.session['image'] = cpuser[0].image.url
        if(len(cpuser)==1):
            context['clubProfile']= cpuser[0]  
        user = ClubProfile.objects.filter(user=request.user)
        if len(cpuser)==1:
            codingProfile = CodingProfile.objects.filter(user=cpuser[0])
            if len(codingProfile)==1:
                context['codingProfile'] = codingProfile[0]
        if len(user)==1:
            profile = Profile.objects.filter(user=cpuser[0])
            if len(profile)==1:
                context['personalProfile'] = profile[0]
        if len(user)==1:
            skills = Skill.objects.filter(user=cpuser[0])
            print(skills)
            if len(skills)>0:
                context['skills'] = skills
        if len(user)==1:
            education = Education.objects.filter(user=cpuser[0])
            if len(profile)==1:
                context['educationProfiles'] = education
    except:
        pass      
    return render(request,'dashboard/profile/personal_profile.html',context)


""" Function to add articles """
@login_required
def add_articles(request):
    if request.method == "POST":
        try:
            cf = ClubProfile.objects.filter(user=request.user)
            # print(cf[0].name)
            user = request.user
            author = cf[0].name
            Title = request.POST['title']
            Domain = request.POST['domain']
            Highlights = request.POST['highlights']
            Description = request.POST['Description']
            SubHeading = request.POST['SubHeading']
            Content = request.POST['Content']
            Code = request.POST['Code']
            quoteBy = request.POST['quoteBy']
            Quote = request.POST['Quote']
            Tag1 = request.POST['Tag1']
            Tag2 = request.POST['Tag2']
            Tag3 = request.POST['Tag3']
            try:
                TImage = request.FILES['TImage']
            except:
                TImage = None
            slug = slugify(user) +"-"+ slugify(Domain+ " " + Title)+"-"+ get_random_string(10,'012innogeeks3456789')
            try:
                Image = request.FILES['Image']
            except:
                Image =None
            inst = Article(user=user,author = author, slug=slug, title= Title,quoteBy=quoteBy, domain= Domain, highlights = Highlights, description= Description, content=Content, code= Code, subHeading=SubHeading, quote=Quote, tag1=Tag1, tag2=Tag2, tag3=Tag3, Thumbimage1 = TImage,Thumbimage2 = Image)
            inst.save()
            messages.success(request,'Article Added Successfully')
            return redirect('article_list')
        except:
            messages.error(request, 'An error occurred, Contact to team')
            return redirect('add_articles')        
    return render(request,'dashboard/articles/add_articles.html')


""" Function to display all articles """
@login_required
def article_list(request):
    atcls = Article.objects.order_by('-date').filter(user=request.user)
    # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(atcls,6)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:   
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles': articles}
    user = request.user
    return render(request,'dashboard/articles/article_list.html',context) 


""" Function to delete article """
@login_required
def delete_article(request,pk):
    try:
        article = Article.objects.get(pk=pk, user=request.user)
        article.delete()
        messages.success(request, 'Article was successfully deleted')
        return redirect('article_list')
    except:
        messages.error(request, 'Some error occured. Kindly contact the team.')
        return redirect('article_list')       


""" Function to update article """
@login_required
def update_article(request,pk):
    try:
        if request.method == "POST":
            article = Article.objects.get(user=request.user, id=pk)
            article.title = request.POST['Title']
            article.domain = request.POST['Domain']
            article.highlights = request.POST['Highlights']
            article.description = request.POST['Description']
            article.subHeading = request.POST['SubHeading']
            article.content = request.POST['Content']
            article.code = request.POST['Code']
            article.quote = request.POST['Quote']
            article.tag1 = request.POST['Tag1']
            article.tag2 = request.POST['Tag2']
            article.tag3 = request.POST['Tag3']
            article.quoteBy = request.POST['quoteBy']
            try:
                article.Thumbimage1 = request.FILES['TImage']
            except:
                pass
            user = request.user
            Domain= request.POST['Domain']
            Title = request.POST['Title']
            # article.slug= slugify(user) +"-"+ slugify(Domain+ " " + Title)+"-"+ get_random_string(10,'012innogeeks3456789')
            try:
                article.Thumbimage2 = request.FILES['Image']
            except:
                pass
            article.save()
            messages.success(request,'Article Updated successfully')
            return redirect('article_list')          
        article = Article.objects.get(user=request.user, id=pk)
        return render(request,'dashboard/articles/update_article.html',{'article':article})
    except:
        return redirect('404_not_found')


""" Function to add project """
@login_required
def add_project(request):
    if request.method == "POST":
        try:
            User = request.user
            ProjectName = request.POST['ProjectName']
            Description = request.POST['Description']
            TeamMembers = request.POST['TeamMembers']
            Category = request.POST['Category']
            TechUsed = request.POST['TechUsed']
            Is_public = True if request.POST['is_public'] =='public' else False 
            GithubURL = request.POST['GithubURL']
            VideoURL = request.POST['VideoURL']
            YourRole = request.POST['YourRole']
            Time = request.POST['Time']
            YourRole = request.POST['YourRole']
            try:
                Image = request.FILES['Image']
            except:
                Image = None
            inst = Project(user=User, projectName= ProjectName, category= Category, techUsed= TechUsed, description= Description, teamMembers= TeamMembers, videoURL= VideoURL, githubURL= GithubURL, yourRole= YourRole, time= Time,is_public = Is_public, image= Image )
            inst.save()
            return redirect('project')
        except:
            messages.error(request, 'An error occurred, Contact the team')
            return redirect('add_project')
    return render(request,'dashboard/projects/add_project.html')


""" Function to delete preject"""
@login_required
def delete_project(request,pk):
    try:
        project = Project.objects.get(pk=pk, user=request.user)
        project.delete()
        messages.success(request, 'Project Successfully Deleted!')
        return redirect('project')
    except:
        messages.error(request, 'An error occurred, Kindly contact the team')
        return redirect('project')
        

""" Function to update project """
@login_required
def update_project(request,pk):
    try:
        if request.method == "POST":
            project = Project.objects.get(user=request.user, id=pk)
            project.projectName = request.POST['ProjectName']
            project.description = request.POST['Description']
            project.teamMembers = request.POST['TeamMembers']
            project.category = request.POST['Category']
            project.techUsed = request.POST['TechUsed']
            project.is_public = True if request.POST['is_public'] =='public' else False 
            project.githubURL = request.POST['GithubURL']
            project.videoURL = request.POST['VideoURL']
            project.yourRole = request.POST['YourRole']
            project.time = request.POST['Time']
            try:
                project.image = request.FILES['Image'] 
            except: 
                pass
            project.save()
            messages.success(request,'Updated successfully')
            return redirect('project')          

        project = Project.objects.get(user=request.user, id=pk)
        return render(request,'dashboard/projects/update_project.html',{'project':project})
    except:
        return redirect('404_not_found')


""" Function to display list of all projects"""
@login_required
def project(request):
    prjs = Project.objects.order_by('-date').filter(user=request.user)
    # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(prjs,6)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:   
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {'projects': projects}
    return render(request,'dashboard/projects/project_list.html',context)


""" Function to display upcoming hacakathons (created by admin)"""
@login_required
def hackathon(request):
    hack = upcomingHackathon.objects.order_by('-date').filter(is_active = True)
    page = request.GET.get('page',1)
    
    paginator = Paginator(hack,8)
    try:
        hackathons = paginator.page(page)
    except PageNotAnInteger:   
        hackathons = paginator.page(1)
    except EmptyPage:
        hackathons = paginator.page(paginator.num_pages)

    context = {'hackathons':hackathons}   
    return render(request,'dashboard/hackathons/hackathon.html', context)


""" Function to add hackathons"""
@login_required
def add_hackathon(request):
    if request.method == "POST":
        try:
            HackathonName = request.POST['HackathonName']
            Achievement = request.POST['achievement']
            Prize = request.POST['Prize']
            Certificate = request.POST['Certificate']
            TeamName = request.POST['TeamName']
            TeamMembers = request.POST['TeamMembers']
            TechStack = request.POST['TechStack']
            YourRole = request.POST['YourRole']
            Description = request.POST['Description']
            try:
                Image = request.FILES['Image']
            except:
                Image = None
            is_public =  True if request.POST['is_public']=='public' else False
            inst = Hackathon(hackathonName=HackathonName, achievement=Achievement, prize= Prize, certificate=Certificate, teamMembers=TeamMembers, teamName=TeamName, techStack=TechStack, yourRole=YourRole, description=Description, image= Image,user=request.user, is_public=is_public)
            inst.save()
            messages.success(request,'Hackathon details added successfully')
            return redirect('hackathon_list')
        except:
            messages.error(request,'error occured, kindly contact the team')
            return redirect('home')
    return render(request,'dashboard/hackathons/add_hackathon.html')


""" Function to delete hackathons """
@login_required
def delete_hackathon(request,pk):
    try:
        hackathon = Hackathon.objects.get(pk=pk, user=request.user)
        hackathon.delete()
        messages.success(request, 'Hackathon details deleted successfully')
        return redirect('hackathon_list')
    except:
        messages.error(request,'error occured, kindly contact the team')
        return redirect('hackathon_list')


""" Function to update hackathons"""
@login_required
def update_hackathon(request,pk):
    try:    
        if request.method == "POST":
            hackathon = Hackathon.objects.get(user=request.user, id=pk)
            hackathon.hackathonName = request.POST['HackathonName']
            hackathon.achievement = request.POST['achievement']
            hackathon.prize = request.POST['Prize']
            hackathon.certificate = request.POST['Certificate']
            hackathon.teamName = request.POST['TeamName']
            hackathon.teamMembers = request.POST['TeamMembers']
            hackathon.techStack = request.POST['TechStack']
            hackathon.yourRole = request.POST['YourRole']
            hackathon.description = request.POST['Description']
            try:
                hackathon.image = request.FILES['Image']
            except:
                pass
            hackathon.is_public =  True if request.POST['is_public']=='public' else False
            hackathon.save()
            messages.success(request,'Updated successfully')
            return redirect('hackathon_list')          
        hackathon = Hackathon.objects.get(user=request.user, id=pk)
        return render(request,'dashboard/hackathons/update_hackathon.html',{'hackathon':hackathon})
    except:
        return redirect('404_not_found')


""" Function to display hackathon list"""
@login_required
def hackathon_list(request):
    hacks = Hackathon.objects.order_by('-date').filter(user=request.user)
    # Pagination
    page = request.GET.get('page',1)
    paginator = Paginator(hacks,2)
    try:
        hackathons = paginator.page(page)
    except PageNotAnInteger:   
        hackathons = paginator.page(1)
    except EmptyPage:
        hackathons = paginator.page(paginator.num_pages)

    return render(request,'dashboard/hackathons/hackathon_list.html',{'hackathons':hackathons})


""" Function to display public profile"""
@login_required
def public_profile(request):
    return render(request,'dashboard/profile/public_profile.html')


""" Function to display resume [code for Update then save & display]"""
@login_required
def resume(request):
    if request.method == "POST":       
        try:
            resume= Resume.objects.get(user= request.user)
            resume.firstName = request.POST['FirstName']
            resume.lastName = request.POST['LastName']
            resume.bio = request.POST['Bio']
            resume.email = request.POST['Email']
            resume.otherInfo1 = request.POST['OtherInfo1']
            resume.otherInfo2 = request.POST['OtherInfo2']
            resume.facebook = request.POST['Facebook']
            resume.twitter = request.POST['Twitter']
            resume.instagram = request.POST['Instagram']
            resume.linkedin = request.POST['Linkedin']
            resume.skype = request.POST['Skype']
            resume.github = request.POST['Github']
            resume.save()           
        except:
            FirstName = request.POST['FirstName']
            LastName = request.POST['LastName']
            Bio = request.POST['Bio']
            Email = request.POST['Email']
            OtherInfo1 = request.POST['OtherInfo1']
            OtherInfo2 = request.POST['OtherInfo2']
            Facebook = request.POST['Facebook']
            Twitter = request.POST['Twitter']
            Instagram = request.POST['Instagram']
            Linkedin = request.POST['Linkedin']
            Skype = request.POST['Skype']
            Github = request.POST['Github']
            ins = Resume(user =request.user, firstName = FirstName, lastName= LastName, bio= Bio, email=Email, otherInfo1=OtherInfo1, otherInfo2= OtherInfo2, facebookURL= Facebook, twitterURL= Twitter, instagramURL= Instagram, linkedinURL= Linkedin, skypeURL= Skype, githubURL= Github)
            ins.save()              
    resume = Resume.objects.filter(user=request.user)
    context ={'resume' : {}}
    if(len(resume)==1):
        context = {'resume': resume[0]}  
    return render(request,'dashboard/profile/resume.html',context)


""" Function to assign tasks"""
@login_required
def assign_task(request):
    return render(request,'dashboard/mentor/Assign-Task.html')


""" Function to manage task"""
@login_required
def manage_task(request):
    return render(request,'dashboard/mentor/Manage-Task.html')


""" Function to view student task """
@login_required
def student_task(request):
    return render(request,'dashboard/mentor/student-task.html')


""" Function to view task updates"""
@login_required
def mentor_update(request):
    return render(request,'dashboard/mentor/updates.html')


""" Function to display detailed resources of a acategory of domain"""
@login_required
def resources_links(request,category,subtopic): 
    try:
        course = Course.objects.get(name=category)
        clubprofile = ClubProfile.objects.get(courses=course, user=request.user)
        topics = Topic.objects.filter(domain=course)
        subtopics = SubTopic.objects.filter(topic__in=topics)
        exact_subtopic = subtopics.get(subtopic_name=subtopic)
        vds = VideoLecture.objects.order_by("-date").filter(subtopic=exact_subtopic)
        pdfs = PDF.objects.filter(subtopic=exact_subtopic)
        otherLinks = OtherLink.objects.filter(subtopic=exact_subtopic)
        stopics = SubTopic.objects.filter(subtopic_name =exact_subtopic)
        contents = Content.objects.filter(subtopic=exact_subtopic)
        # Pagination
        page = request.GET.get('page',1)
        paginator = Paginator(vds,8)
        try:
            videolectures = paginator.page(page)
        except PageNotAnInteger:   
            videolectures = paginator.page(1)
        except EmptyPage:
            videolectures = paginator.page(paginator.num_pages)

        context = {'stopic':subtopics[0], 'videolectures': videolectures,'pdfs': pdfs,'contents':contents,'otherLinks':otherLinks,'subtopic':exact_subtopic}
        return render(request, 'dashboard/resources/links.html', context)
    except:
        return redirect('404_not_found')


""" Function to display all the available resources of a domain"""
@login_required
def resource_home(request,category):
    try:
        course = Course.objects.get(name=category)
        clubprofile = ClubProfile.objects.get(courses=course, user=request.user)
        topics = Topic.objects.filter(domain=course)    
        subtopics = SubTopic.objects.filter(topic__in=topics)
        context = {'topics': topics, 'subtopics': subtopics,'course': course}
        return render(request, 'dashboard/resources/resources.html',context)
    except:
        return redirect('404_not_found')


""" Function to render 404 page"""
def not_found404(request):
    return render(request, 'dashboard/404.html')


""" Function for feedback"""
def feedback(request):
    return render(request, 'dashboard/feedback.html')


