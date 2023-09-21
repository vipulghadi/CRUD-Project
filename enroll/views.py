from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegister
from .models import User

# Create your views here.
# adding new data
def add_show(request):
    data=User.objects.all()
    if request.method=="POST":
        fm=StudentRegister(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data["name"]
            email=fm.cleaned_data["email"]
            password=fm.cleaned_data["password"]
            reg=User(name=name,email=email,password=password)
            reg.save()
            data=User.objects.all()
            
            fm=StudentRegister()
           
       # fm.save() direct method to save data
    else:
        fm=StudentRegister() 
        data=User.objects.all()    
    return render(request,'enroll/addandshow.html',{"form":fm,"data":data})

# deleting the data
def delete_data(request,id):
    if request.method=="POST":
        
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
    

#updating value
def update(request,id):
    
    if request.method=="POST":
        
        pi=User.objects.get(pk=id)
        fm=StudentRegister(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
           
        return HttpResponseRedirect("/")
        
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegister(instance=pi) 
        
    return render(request,"enroll/update.html",{"fm":fm})