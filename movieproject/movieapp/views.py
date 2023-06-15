from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie1=movie.objects.all()
    context={
        "movie_list":movie1
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie2=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie2})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie3=movie(name=name,desc=desc,year=year,img=img)
        movie3.save()
    return render(request,"add.html")

def update(request,id):
    movie4=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie4)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie5=movie.objects.get(id=id)
        movie5.delete()
        return redirect('/')
    return render(request,'delete.html')
