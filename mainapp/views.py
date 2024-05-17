from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate, logout
from django.contrib.auth  import login as auth_login
from  .flexapi import FlexUnlimited

from django.shortcuts import render , redirect
# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def  pricing(request):
    return render(request,'Pricing.html')


def Service(request):
    return render(request,'service.html')

def support(request):
    return render(request,'Support.html')


def  signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'signup.html')

        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'signup.html')
    
        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'signup.html')

        # Create the user
        user = User.objects.create_user(username, email, password)
       
        user.save()
        # flex_api = FlexUnlimited()
        # print('eeee')
        # flex_api.run() # Modify as per FlexUnlimited API
           # Modify as per FlexUnlimited API
            
        # user.save()
        # current_site = get_current_site(request)
        # email_body = {
        #             'user': user,
        #             'domain': current_site.domain,
        #             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #             'token': account_activation_token.make_token(user),
        #         }

        # link = reverse('activate', kwargs={
        #                        'uidb64': email_body['uid'], 'token': email_body['token']})

        # email_subject = 'Activate your account'

        # activate_url = 'http://'+current_site.domain+link

        # emailsend = EmailMessage(
        #             email_subject,
        #             'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
        #             'testingapp895@gmail.com',
        #             [email],
        #         )
        # emailsend.send(fail_silently=False)
        messages.success(request, "Your Account is created")
        return render(request, 'signup.html')
            
      
    return render(request, 'signup.html')



def login(request):
       if request.method == "POST":
        # Get the post parameters
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  
        if user is not None:
           
            auth_login(request  , user)
            # flex_api = FlexUnlimited()
            # flex_api.authenticate(username, password) 
            return redirect('/')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "login.html")
       return render(request, 'login.html')


def Userlogout(request):
    logout(request)
    return redirect('/login')

