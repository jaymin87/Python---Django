from django.shortcuts import render, redirect
from .models import Member
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    members = Member.objects.all()
    paginator = Paginator(members, 10)
    page = request.GET.get('page')
    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)
    return render(request, 'crud/index.html', {'context': context} )

def create(request):
    member = Member(id=6,Description=request.POST['Description'],
    Lattitude=request.POST['Lattitude'],
		Longitude=request.POST['Longitude'],
		Elevation=request.POST['Elevation'],
		CreatedDate=request.POST['CreatedDate'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.Description = request.POST['Description']
    member.Lattitude = request.POST['Lattitude']
    member.Longitude = request.POST['Longitude']
    member.Elevation = request.POST['Elevation']
    member.CreatedDate = request.POST['CreatedDate']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')