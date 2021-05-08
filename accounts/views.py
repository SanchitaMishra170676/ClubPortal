from django.contrib.auth import logout as auth_logout, login as auth_login
from django.shortcuts import render,redirect,HttpResponse,Http404
from django.contrib import messages
from django.contrib.auth import authenticate
from dashboard.models import ClubProfile
from django.contrib.auth.models import User
from dashboard.models import Course
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.core import mail

# Create your views here.

def login(request):
    if request.method =='POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username =loginusername,password =loginpassword)
        
        
        if user is not None  :
            clubProfile = ClubProfile.objects.filter(user=user)
            if len(clubProfile)==1 and clubProfile[0].is_active==True:
                auth_login(request,user)
                messages.success(request,'Logged in Successfully')
                return redirect('home')
            else:
                messages.success(request,"ClubProfile doesn't exist, Contact to Core Team!")
                return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    if request.user.is_authenticated:
        return HttpResponse('404 not found')
    else:
        return render(request,'home/login.html')

def handlelogout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request,'successfully logged out')
        return redirect('home')
    else:
        return HttpResponse('404 Not found')

def password_reset(request):
    return render(request,'home/password_reset.html')


def password_reset_confirm(request):
    return render(request,'home/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request,'home/password_reset_complete.html') 

def password_reset_email(request):
    return render(request,'home/password_reset_email.html')



def registration(request):
    if request.user.is_authenticated:
        return redirect('404_not_found')

    if request.method == "POST":
        
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        Gender = request.POST['Gender']
        Branch = request.POST['Branch']
        # Section = request.POST['Section']
        
        HostelStatus = request.POST['HostelStatus']
        Email = request.POST['Email']
        CollegeEmail = request.POST['CollegeEmail']
        PhoneNo = request.POST['PhoneNo']
        Batch = request.POST['Batch']
        try:
            Image = request.FILES['Image']
        except:
            Image=None
        Domain = request.POST['Domain']
        
        Password = request.POST['Password']
        ConfirmPassword = request.POST['ConfirmPassword']
        
        r = CollegeEmail.split("@")[0] 
        username =  'innogeeks.' + r.split('.')[-1]  
        # print(username)
        user = User.objects.filter(username=username)
        # print(Email,CollegeEmail)

        if len(user)!=0:
            messages.error(request,'profile already exists, pls contact to core team')
            return redirect('home')
        if len(Password)<8:
            messages.error(request,"Your password must be atleast of 8 characters")
            return redirect('register')
        if Password != ConfirmPassword:
            messages.error(request,"Your password doesn't match!")
            return redirect('register')
        
        
        
        
        user = User.objects.create_user(username=username, password=Password)
        user.first_name = FirstName
        user.last_name = LastName
        user.email = CollegeEmail

        user.save()


        clubProfile = ClubProfile(
            name=FirstName+' '+LastName,
            user= user,
            image= Image,
            gender=Gender,
            branch=Branch,
            phone=PhoneNo,
            personal_email = Email,
            college_email = CollegeEmail,
            domain = Domain,
            batch = Batch,
            hostel_status= HostelStatus,
            is_active = False,
            is_mentor = False
            )
        courses = []
        try:
            courses.append(Course.objects.get(name=Domain).id)
        except:
            course = Course(name=Domain)
            course.save()
            courses.append(course.id)
        
        try:
            courses.append(Course.objects.get(name="Basic Programming").id)
        except:
            course = Course(name="Basic Programming")
            course.save()
            courses.append(course.id)
            
        try:
            courses.append(Course.objects.get(name="DSA").id)
        except:
            course = Course(name="DSA")
            course.save()
            courses.append(course.id)
        clubProfile.save()
        clubProfile.courses.set(courses)
        clubProfile.save() 

        try:
            # messages.success(request,'Registration Successful!, The account will be activated soon')
            connection = mail.get_connection()
            connection.open()
            message= render_to_string('emails/registrationSuccessful.html',{})
            email_ver =  EmailMessage(
            "Registration Successful!",
            message
            ,to=[CollegeEmail])    
            
        # email_ver.fail_silently=False,
            email_ver.content_subtype = 'html'
            email_ver.send()
            connection.close()
        except :
            pass   
    

        

        messages.success(request,'Registered Successfully!, Credentials will be Provided Soon!')
        return redirect('home')

    
            
    return render(request, 'home/registration.html')

