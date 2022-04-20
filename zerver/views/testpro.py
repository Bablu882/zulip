from django.shortcuts import render
from django.shortcuts import render,redirect
from zerver.forms import UserRegistration
from zerver.models import User
from django.http import HttpResponse


def hello(request):
    return render(request,'zerver/app/testpro.html')






# Create your views here.
def addshow(request):
    if request.method=='POST':
        frm=UserRegistration(request.POST)
        if frm.is_valid():
            frm.save()
            frm=UserRegistration() 
    else:
        frm=UserRegistration() 
    name=User.objects.all()
       
    return render(request,'zerver/app/addshow.html',{'form':frm,'users':name})


def update(request,id):
    request.method=='POST'
    gt=User.objects.get(pk=id)
    gte=UserRegistration(request.POST,instance=gt)
    if gte.is_valid():
        gte.save()
        gte=UserRegistration()

    else:
        gt=User.objects.get(pk=id)
        gte=UserRegistration(instance=gt)
    return render(request,'zerver/app/edit.html',{'frm':gte})
    

def delete(request, id):
    User.objects.filter(id=id).delete()

    return redirect('/addshow')


