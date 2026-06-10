from django.shortcuts import render, redirect

from .models import *
from django.http import HttpResponse
# Create your views here.
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
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()

    return redirect("/recipes/") 