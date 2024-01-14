from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistraion
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistraion(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=User(name=em,email=em,password=ps)
            reg.save()
            fm=StudentRegistraion()
    else:
        fm=StudentRegistraion()   
        stud=User.objects.all() 
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method == "POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistraion(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistraion(instance=pi)
            
    return render(request,'enroll/updateStudent.html',{'form':fm})



def delete_data(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')