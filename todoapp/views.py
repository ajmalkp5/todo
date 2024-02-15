from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp.models import Todotype
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class Registrationform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]



class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()




class Todotypeform(forms.ModelForm):

    class Meta:
        model=Todotype
        exclude=("created_date",)

class Todotypelistview(View):
    def get(self,request,*args,**kwargs):
        qs=Todotype.objects.all()
        return render(request,"todo_list.html",{"data":qs})
    
class todocreateview(View):
    def get(self,request,*args,**kwargs):
        form=Todotypeform()
        return render(request,"todo_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Todotypeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
        else:
            return render(request,"todo_add.html",{"form":form})
        

class Tododetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todotype.objects.get(id=id)
        return render(request,"todo_detail.html",{"data":qs})
    

class Tododeleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todotype.objects.filter(id=id).delete()
        return redirect("todo-list")
    

class Todoupdateview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        todo_object=Todotype.objects.get(id=id)
        form=Todotypeform(instance=todo_object)
        return render(request,"todo_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        todo_object=Todotype.objects.get(id=id)
        form=Todotypeform(request.POST,instance=todo_object)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
        else:
            return render(request,"todo_edit.html",{"form":form})


# signup
        
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Registrationform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print("success")
            return redirect("signin")
        else:
            print("failed")
            return render(request,"registration.html",{"form":form})
    


class Signinview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(u_name,pwd)
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("todo-list")
            
        return render(request,"login.html",{"form":form})
    

class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
