from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .models import foodmodel
from menufriend_algorithm import mf_main
import csv
import pandas as pd
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login_view(request):
    
    Users = User.objects.get(username='test')
    
    Users_1=Users.견과류
    Users_1=float(Users_1)
    Users_2 = Users.곡물전분류
    Users_2 = float(Users_2)
    Users_3 = Users.기타
    Users_3 = float(Users_3)
    Users_4 = Users.김치류
    Users_4 = float(Users_4)
    Users_5 = Users.난류
    Users_5 = float(Users_5)
    Users_6 = Users.면류
    Users_6 = float(Users_6)
    Users_7 = Users.버섯류
    Users_7 = float(Users_7)
    Users_8 = Users.유제품
    Users_8 = float(Users_8)
    Users_9 = Users.육류
    Users_9 = float(Users_9)
    Users_10 = Users.조리가공품류
    Users_10 = float(Users_10)
    Users_11 = Users.조미료
    Users_11 = float(Users_11)
    Users_12 = Users.채소류
    Users_12 = float(Users_12)
    Users_13 = Users.해산물
    Users_13 = float(Users_13)

    


    
    
    
    
    user_1 = [{'견과류': Users_1, '곡물전분류': Users_2, '기타': Users_3, '김치류': Users_4, '난류': Users_5, '면류': Users_6, '버섯류': Users_7, 
    '유제품': Users_8, '육류': Users_9, '조리가공품류': Users_10, '조미료': Users_11, '채소류': Users_12, '해산물': Users_13},[]]
    #print(f'mf_1500{user_1[1]}:',mf_main(1,user_1,1,10))
    mf_main_10 = mf_main(1, user_1, 1, 10)
    
    
    df1 = pd.read_csv(r"C:\Users\opeer\here\here_1\AI SCHOOL\main\main_1\gj_ai_main_team9\menufriend\gj_ai_main_team9-min\mfd.csv", encoding = 'utf-8')
    testing=df1.iloc[mf_main_10]
    # testing2=testing[1]

    # menu_1=df1.iloc[mf_main_10[0]]
    # menu_1_1=df1.iloc[mf_main_10[0]][1]
    # menu_2=df1.iloc[mf_main_10[1]]
    # menu_3=df1.iloc[mf_main_10[2]]
    # menu_4=df1.iloc[mf_main_10[3]]
    # menu_5=df1.iloc[mf_main_10[4]]
    # menu_6=df1.iloc[mf_main_10[5]]
    # menu_7=df1.iloc[mf_main_10[6]]
    # menu_8=df1.iloc[mf_main_10[7]]
    # menu_9=df1.iloc[mf_main_10[8]]
    # menu_10=df1.iloc[mf_main_10[9]]
    #  # munu_1부터 선호도 높은음식 [1]부터 제목 /_1= 제목 _2 = 분류 _3=재료, _4= 재료,분류 _5=재료,분류 _6=조리법, 7=종류, 8=시간, 9=난이도
    # menu_1_1 = menu_1[1]
    # menu_2_1 = menu_2[1]
    # menu_3_1 = menu_3[1]
    # menu_4_1 = menu_4[1]
    # menu_5_1 = menu_5[1]
    # menu_6_1 = menu_6[1]
    # menu_7_1 = menu_7[1]
    # menu_8_1 = menu_8[1]
    # menu_9_1 = menu_9[1]
    # menu_10_1 = menu_10[1]
    



    
    context = {'testing':testing,'Users':Users, 'mf_main_10':mf_main_10, 'mf_main_10_0':mf_main_10[0], 'mf_main_10_1':mf_main_10[1], 'mf_main_10_2':mf_main_10[2], 'mf_main_10_3':mf_main_10[3], 'mf_main_10_4':mf_main_10[4], 'mf_main_10_5':mf_main_10[5], 'mf_main_10_6':mf_main_10[6], 'mf_main_10_7':mf_main_10[7], 'mf_main_10_8':mf_main_10[8], 'mf_main_10_9':mf_main_10[9]}
    #'mf_main_10_0':mf_main_10[0], 'mf_main_10_1':mf_main_10[1], 'mf_main_10_2':mf_main_10[2], 'mf_main_10_3':mf_main_10[3], 'mf_main_10_4':mf_main_10[4], 'mf_main_10_5':mf_main_10[5], 'mf_main_10_6':mf_main_10[6], 'mf_main_10_7':mf_main_10[7], 'mf_main_10_8':mf_main_10[8], 'mf_main_10_9':mf_main_10[9]




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



