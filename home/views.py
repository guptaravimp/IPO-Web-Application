from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import IPOUpcoming, FaqModel
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {'error': 'Username already exists'})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/')
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "signin.html", {'error': 'Invalid credentials'})
    return render(request, "signin.html")

def logoutUser(request):
    logout(request)
    return redirect("/")

def broker(request):
    return render(request, "brokers.html")

def ipoupcomming(request):
    ipoupcommingdata=IPOUpcoming.objects.all()
    faqadmindata=FaqModel.objects.all()
    data={
        'ipoupcommingdata': ipoupcommingdata,
        'faqadmindata': faqadmindata
    }
    return render(request, "ipoupcomming.html",data)

def community(request):
    return render(request, "community.html")

def products(request):
    return render(request, "products.html")
