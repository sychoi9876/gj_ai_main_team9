from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .models import foodmodel
from menufriend_algorithm import mf_main

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_view(request):
    
    Users = User.objects.get(username='test')
    

    
    
    
    
    user_1 = [{'견과류': Users.견과류, '곡물전분류':Users.곡물전분류, '기타': Users.기타, '김치류': 3, '난류': 1, '면류': 3, '버섯류': 1, 
    '유제품': 1, '육류': 1, '조리가공품류': 1, '조미료': 1, '채소류': 3, '해산물': 3},[]]
    #print(f'mf_1500{user_1[1]}:',mf_main(1,user_1,1,10))
    mf_main_10 = mf_main(1, user_1, 1, 10)
    context = {'Users':Users, 'mf_main_10':mf_main_10, 'mf_main_10_1':mf_main_10[1]}




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
            곡물전분류 = request.POST["곡물전분류"]
            김치류 = request.POST["김치류"]
            난류 = request.POST["난류"]
            면류 = request.POST["면류"]
            버섯류 = request.POST["버섯류"]
            유제품 = request.POST["유제품"]
            육류 = request.POST["육류"]
            조리가공품류 = request.POST["조리가공품류"]
            채소류 = request.POST["채소류"]
            해산물 = request.POST["해산물"]
            견과류 = request.POST["견과류"]
            조미료 = request.POST["조미료"]
            기타 = request.POST["기타"]




            user = User.objects.create_user(username, email, password)
            user.name = name
            user.height = height
            user.weigth = weight
            user.gender = gender
            user.곡물전분류 = 곡물전분류
            user.김치류 = 김치류
            user.난류 = 난류
            user.면류 = 면류
            user.버섯류 = 버섯류
            user.유제품 = 유제품
            user.육류 = 육류
            user.조리가공품류 = 조리가공품류
            user.채소류 = 채소류
            user.해산물 = 해산물
            user.기타 = 기타
            user.조미료 = 조미료
            user.견과류 = 견과류

                        
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



