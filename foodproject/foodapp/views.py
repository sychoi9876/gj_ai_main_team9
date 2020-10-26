from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_view(request):
    context = {}

    if request.method =="POST":
        if request.POST["username"] and request.POST['password']:

            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       
            if user is not None:
                print("인증성공")
                login(request, user)
            else:
                print("인증실패")
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
    
        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    context = {}


    if request.method =="POST":
        if (request.POST['username'] and request.POST['password'] and request.POST['password'] == request.POST['password2']):
            
            username = request.POST["username"]
            name = request.POST["name"]
            password = request.POST["password"]
            email = request.POST["email"]

            user = User.objects.create_user(username, email, password)
            user.name = name
            user.save()
        
            return redirect("login")

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

    return render(request, 'signup.html', context)


def recipe1(request):
    return render(request, 'recipe1.html')