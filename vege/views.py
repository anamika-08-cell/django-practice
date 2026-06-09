from django.shortcuts import render, redirect
from .models import *
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
    context = { 'recipes': queryset}
                               
    return render(request,'recipes.html',context)
