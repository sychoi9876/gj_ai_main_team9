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
            height = request.POST["height"]
            weight = request.POST["weight"]
            gender = request.POST["gender"]
            밥빵 = request.POST["밥빵"]
            김치류 = request.POST["김치류"]
            난류 = request.POST["난류"]
            면류 = request.POST["면류"]
            버섯류 = request.POST["버섯류"]
            유제품 = request.POST["유제품"]
            육류 = request.POST["육류"]
            조리가공식품류 = request.POST["조리가공식품류"]
            채소류 = request.POST["채소류"]
            해산물 = request.POST["해산물"]




            user = User.objects.create_user(username, email, password)
            user.name = name
            user.height = height
            user.weigth = weight
            user.gender = gender
            user.밥빵 = 밥빵
            user.김치류 = 김치류
            user.난류 = 난류
            user.면류 = 면류
            user.버섯류 = 버섯류
            user.유제품 = 유제품
            user.육류 = 육류
            user.조리가공식품류 = 조리가공식품류
            user.채소류 = 채소류
            user.해산물 = 해산물

                        
            user.save()
        
            return redirect("login")

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

    return render(request, 'signup.html', context)


def recipe1(request):
    return render(request, 'recipe1.html')


def recipe_1(request):
    return render(request, 'recipe_1.html')

def recipe_2(request):
    return render(request, 'recipe_2.html')

def recipe_3(request):
    return render(request, 'recipe_3.html')

def recipe_4(request):
    return render(request, 'recipe_4.html')

def recipe_5(request):
    return render(request, 'recipe_5.html')