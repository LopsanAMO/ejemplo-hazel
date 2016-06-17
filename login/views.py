from django.shortcuts import render, redirect
from .forms import UsuarioForm, LogForm
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Registrar(View):
    def get(self, request):
        template_name = 'formi.html'
        form = UsuarioForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        form = UsuarioForm(request.POST, request.FILES)
        username = request.POST.get('nombre', None)
        password = request.POST.get('boleta', None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/login/login')
        else:
            return redirect('/login/registrar')

class Login(View):
    def get(self, request):
        template_name = 'login.html'
        form = LogForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('boleta')
        form = LogForm(request.POST)
        if form.is_valid():
            print (username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/proyecto/casi')
        else:
            return redirect('/login/login')

class Index(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)

def Logout(request):
    logout(request)
    return redirect('/proyecto/casi')
