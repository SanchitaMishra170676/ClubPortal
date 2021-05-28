from django.shortcuts import render,redirect
from django.template.defaultfilters import slugify
from dashboard.models import ClubProfile, Article,Resume, Project, Achievement
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import  (CodingProfile, Profile, Skill, Education,) 
# Create your views here.

""" Function for coding profiles [Update -> Save] """
@login_required
def coding_profile(request):
    if request.method == 'POST':
        try:
            cpuser =ClubProfile.objects.get(user=request.user)   
            try:
                codingProfile = CodingProfile.objects.get(user=cpuser)
                codingProfile.codechef = request.POST['codechef']
                codingProfile.codeforces = request.POST['codeforces']
                codingProfile.spoj = request.POST['spoj']
                codingProfile.interviewbit = request.POST['interviewbit']
                codingProfile.leetcode = request.POST['leetcode']
                codingProfile.save()
                messages.success(request,'Coding Profiles updated successfully!')
                return redirect('personal_profile')

            except:
                user = cpuser
                codechef = request.POST['codechef']
                codeforces = request.POST['codeforces']
                interviewbit = request.POST['interviewbit']
                spoj = request.POST['spoj']
                leetcode = request.POST['leetcode']
                codingProfile = CodingProfile(user=user, codeforces=codeforces,codechef=codechef,interviewbit=interviewbit,spoj=spoj,leetcode=leetcode)
                codingProfile.save()
                messages.success(request,'Coding Profiles Created Successfully!')
                return redirect('personal_profile')
            
        except:
            messages.error(request,"No Club profile exist, please contact admin")
            return redirect('personal_profile')
    return redirect('404_not_found')


""" Function to update education details """
@login_required
def personal_profile_education(request,pk):
    if request.method == "POST":    
        try: 
            user = ClubProfile.objects.get(user=request.user)
            education = Education.objects.get(user=user, id=pk)
            education.institution = request.POST['institution']
            education.time_period = request.POST['time_period']
            education.qualification = request.POST['qualification']
            education.grade = request.POST['grade']      
            education.save()

            messages.success(request,"Response updated")
            return redirect('/dashboard/personal_profile/')

        except:
            messages.error(request,"No such qualification exists")
            return redirect('/dashboard/personal_profile/')

    return redirect('404_not_found') 


""" Function to add coding profile details """
@login_required
def education_profile(request):
    if request.method == "POST":
        try:
            user = ClubProfile.objects.get(user=request.user)
            institution = request.POST['institution']
            time_period = request.POST['time_period']
            qualification = request.POST['qualification']
            grade = request.POST['grade']
            education = Education(user=user, institution=institution,qualification=qualification,time_period=time_period,grade=grade)
            education.save()
            messages.success(request,"Added Successfully")
            return redirect('/dashboard/personal_profile/')

        except:
            messages.error(request,"No such qualification exists")
            return redirect('/dashboard/personal_profile/')

    return redirect('404_not_found')


""" Function for personal prfile [Update -> save] """
@login_required
def personal_profile_section(request,section):
    if request.method == "POST":    
        try:
            user = ClubProfile.objects.get(user=request.user)

            if(section == "info_update"):
                try:
                    info = Profile.objects.get( user=user)

                    # info.name = request.POST['Name']
                    uname= request.POST['Username']
                    info.dob= request.POST['Dob']   
                    info.email= request.POST['Email']
                    info.city= request.POST['City']
                    info.state = request.POST['State']
                    info.postal_code = request.POST['Postalcode']
                    info.short_bio = request.POST['Bio']
                    user.name = request.POST['Name']
                    try:
                        info.username = slugify(uname)
                        user.save()
                        info.save()
                    except:
                        messages.error(request,"This username already exist, Kindly enter a unique username")
                        return redirect('/dashboard/personal_profile/')

                
                    messages.success(request,"Response updated")
                    return redirect('/dashboard/personal_profile/')
                except:

                    user.name = request.POST['Name']
                    user.save()
                    Uname = request.POST['Username']
                    Username = slugify(Uname)
                    Dob= request.POST['Dob']
                    Email= request.POST['Email']
                    City= request.POST['City']
                    State = request.POST['State']
                    Postal_code = request.POST['Postalcode']
                    Bio = request.POST['Bio']
                    inst = Profile(user= user, dob = Dob, email=Email, city=City, state=State, username= Username, postal_code=Postal_code,short_bio=Bio)
                    inst.save()
                    messages.success(request,"Sucessfuly Created")
                    return redirect('/dashboard/personal_profile/')

            if(section == "skill_update"):
                try:
                    user = user
                    AddSkill = request.POST['Skill']
                    inst = Skill(user = user, skill=AddSkill)
                    inst.save()
                    messages.success(request,"Sucessfuly Added")
                    return redirect('/dashboard/personal_profile/')
                
                except:
                    messages.error(request,"Some error occured, contact the core team")
                    return redirect('/dashboard/personal_profile/')

        except:
            messages.error(request,"No such credentials exists")
            return redirect('/dashboard/personal_profile/')

    return redirect('404_not_found')


""" Personal profile image """
def personal_image_save(request):
    if request.method == "POST":
        try:
            user = ClubProfile.objects.get(user=request.user)
            print(user)
            if user:
                try:
                    user.image = request.FILES['image']
                    user.save()
                    messages.success(request,"Updated Successfully!")
                except:
                    pass
                return redirect('/dashboard/personal_profile')
            else:
                messages.error(request,"No such Club Profile exists")
        except:
            messages.error(request,"Pls Contact to Core team for Account !")
        return redirect('/dashboard/personal_profile/')



def club_profile_update(request):
    if request.method=='POST':
        pass 


""" Function for education update """
@login_required
def update_education_profile(request,pk):
    if request.method == "POST":    
        try:
            education = Education.objects.get(id=pk, 
            user=ClubProfile.objects.get(user=request.user)
            )
            education.grade = request.POST['grade']
            education.qualification = request.POST['qualification']
            education.time_period = request.POST['time_period']
            education.institution = request.POST['institution']
            education.save()
            messages.success(request,'Qualification Details Updated Successfully!')
            return redirect('home')
        except:
            messages.error(request,"No such qualification exists")
            return redirect('home')
    return redirect('404_not_found')


""" Function to delete education profile """
@login_required
def delete_education_profile(request,pk):
    try:
        education = Education.objects.get(id=pk, 
            user=ClubProfile.objects.get(user=request.user)
            ) 
        messages.success(request,'Education Deleted Successfully!')
        return redirect('home')
    except:
        messages.error(request,"No such qualification exists")
        return redirect('home')
    return redirect('404_not_found')


""" Function to update club profile """
@login_required
def ClubProfiles(request):
        if request.method == "POST":
            try:
                clubProfile = ClubProfile.objects.get(user=request.user)
                clubProfile.branch = request.POST['branch']
                clubProfile.name = request.POST['name']
                clubProfile.phone = request.POST['phone']
                clubProfile.save()
                messages.success(request,'Profile Updated successfully')
                return redirect('home')  
                
            except:
                messages.error(request,"Profile Update Failed")
            return redirect('home')
        return redirect('404_not_found') 



""" Function to delete skills """
@login_required
def delete_skill(request,pk):
    clubProfile = ClubProfile.objects.filter(user=request.user)
    if len(clubProfile)==1:
        try:
            skill = Skill.objects.get(user=clubProfile, id=pk)
            skill.delete()
            messages.success(request,'Skill Deleted successfully')
            return redirect('home')

        except:
            messages.error(request,"Skill delete Failed")
            return redirect('404_not_found')
    else:
        messages.error(request,"No CLub Profile exists")
        return redirect('404_not_found')

""" Function to display Public Proflie"""
def publicProfile(request, the_slug):
    try:      
        profile = Profile.objects.get(username= the_slug)
        iuser = profile.user
        educations = Education.objects.filter(user = iuser)
        skills = Skill.objects.filter(user=iuser)
        projects = Project.objects.order_by('-date').filter(user=iuser.user, is_public = True)
        achievements = Achievement.objects.order_by('-date').filter(user=iuser.user, is_public=True)
        blogs = Article.objects.order_by('-date').filter(user=iuser.user)
        club = ClubProfile.objects.get(user=iuser.user)
        try:
            resume = Resume.objects.get(user = iuser.user)
            context = {'profile':profile, 'educations':educations,'skills':skills, 'projects':projects, 'achievements': achievements,'blogs':blogs, 'resume':resume, 'club':club}
            return render(request, 'dashboard/profile/public_profile.html', context)
        except:
            context = {'profile':profile, 'educations':educations,'skills':skills, 'projects':projects, 'achievements': achievements,'blogs':blogs, 'club':club}
            return render(request, 'dashboard/profile/public_profile.html', context)
    except:
            return render(request, 'dashboard/404.html')        