from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout , login
from Services.models import courses , cloud_computing , software_testing , machine_learning , android_App , ios_App , front_end ,back_end,full_stack

# Create your views here.
def index(request) :
    if request.user.is_anonymous:
        return redirect('/login')
    data = {}
    if request.method == "POST" :
        name = request.POST.get('search')
        data['courses'] = courses.objects.filter(course_name__icontains=name)
    else :
        data['courses'] = courses.objects.all()
    return render(request,"index.html",data)

def dev(request,course) :
    if course == "Cloud Computing" :
        course_details_1 = courses.objects.filter(course_name__icontains="Cloud")
        course_details_2 = cloud_computing.objects.all()
    elif course == "Software Testing" :
        course_details_1 = courses.objects.filter(course_name__icontains="Software")
        course_details_2 = software_testing.objects.all()
    elif course == "Machine Learning" :
        course_details_1 = courses.objects.filter(course_name__icontains="Machine")
        course_details_2 = machine_learning.objects.all()
    elif course == "Android App" :
        course_details_1 = courses.objects.filter(course_name__icontains="Android")
        course_details_2 = android_App.objects.all()
    elif course == "Ios App" :
        course_details_1 = courses.objects.filter(course_name__icontains="Ios")
        course_details_2 = ios_App.objects.all()
    elif course == "Front End Development" :
        course_details_1 = courses.objects.filter(course_name__icontains="Front")
        course_details_2 = front_end.objects.all()
    elif course == "Back End Development" :
        course_details_1 = courses.objects.filter(course_name__icontains="Back")
        course_details_2 = back_end.objects.all()
    elif course == "Full Stack Development" :
        course_details_1 = courses.objects.filter(course_name__icontains="Full Stack")
        course_details_2 = full_stack.objects.all()
    data = {
        'course_details_1' : course_details_1,
        'course_details_2' : course_details_2
    }
    return render(request,"dev.html",data)

def loginUser(request) :
    if request.method == "POST":
        username =  request.POST.get('username')
        password = request.POST.get('password')
        # chect if user has correct credentials
        user = authenticate(username=username, password=password)
        if user is not None  :
            login(request,user)
            return redirect("/")
        else:
            return render(request , 'login.html')

    return render(request , 'login.html')

# sign_up
def sign_up(request) :
    data = {}
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        if password_1 != password_2 :
            data["Re_password"] = True
        if password_1 == "" or password_2 == "":
            data["password"] = True
        if first_name == "" or last_name=="":
            data["first_name"] = True
        if username == "":
            data["Username"] = True
        if email == "":
            data["email"] = True
        elif "@gmail.com" not in email :
            data["email_invalid"] = True
        if first_name != "" and last_name != "" and username != "" and password_1 != "" and password_2 != "" :
            user = User.objects.create_user(username, email, password_1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect("/login")
        return render(request, "sign_up.html" , data)
    return render(request , 'sign_up.html' , data)

def logoutUser(request) :
    logout(request)
    return redirect("/login")