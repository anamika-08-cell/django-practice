from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [{"name" : "anamika","age":19},
         {'name':'hemlata','age': 22},
         {'name':'niharika','age':15},
    ]

    vegetables = ['pumpkin','tomatoes','potatoes']
    return render(request,"home/index.html",context= {'page':'Django 2023 tutorial','peoples':peoples, 'vegetables': vegetables})


def about(request):
    context = {'page':'About'}
    return render(request,"home/about.html", context)

def contact(request):
    context = {'page':'Contact'}
    return render(request,"home/contact.html", context)

def success_page(request):
    return  HttpResponse('<h1>this is a success page</h1>')


