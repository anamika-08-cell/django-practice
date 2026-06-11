from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

#contrib = contribution folder jisme developer ne bani banai(admin panel and session bana rakhe hai).
#auth = authentication subfolder(logout and login related code)
#login browser mai pass ya token save krta hai.
# log out function ka kam session delete krna hota hai.
# without request browser is blind beacuz it carries info about user and  browser both.#if someone is submitting form so also collect data it's neccessary.
# jab aap logout mai request use krte hai to wo  sessions mai wo wali token /id search kr delete kr deta hai.
# request nhi likhne par code crash and type error.

from .models import *
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
         # 2. objects.create() की मदद से डेटाबेस में भेज दिया
        Recipe.objects.create(
            recipe_name = recipe_name, # to store fronted data it's a variable only(write side container)
            recipe_description = recipe_description,
            recipe_image = recipe_image)
        return redirect("/recipes/")
    
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search')) 

    context = { 'recipes': queryset}           
    return render(request,'recipes.html',context)

#for update recipe 
@login_required(login_url='/login/')
def  update_recipe(request,id):
    queryset = Recipe.objects.get(id = id)
    if request.method == "POST":
        # fetch  the data
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save() # save data in database.
        return redirect("/recipes/")
    
    context =  { 'recipe': queryset}
    return render(request,'update_recipe.html',context)


#how to handle dynamic url
@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()

    return redirect("/recipes/") 


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        #here username and password come from html file's name attribute.
        password = request.POST.get('password')
        
        # for checking hashing form and plain form of password-->
        user = authenticate(username=username , password=password)
        if user:
            # store data in login session/relation.
            #request ke ander browser ki cookies ki info hoti hai.
            login(request, user)
            messages.info(request,"Logged in Successfully!")
            return redirect("/recipes/") 
        else:
            messages.error(request, "invalid username or password")
            return redirect("/login/")
    return render(request, 'login.html') #show the login page

def logout_page(request):
    logout(request)
    return redirect("/login/")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "username already taken")
            return redirect("/register/")

        #send it to database.
        user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,   
        )
        
        #for password security.
        user.set_password(password)
        user.save()
        messages.info(request, "account successfully created")
        return redirect("/login/")

    return render(request, 'register.html')