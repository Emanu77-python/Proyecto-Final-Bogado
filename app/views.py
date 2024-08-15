from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, CustomAuthenticationForm



#Create your views here


def inicio(request):
    return render(request, "app/index.html")

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crear_post')
    else:
        form = PublicacionForm()
    
    return render(request, 'app/crear_publicacion.html', {'form': form})

class PublicacionListView(ListView):
    model = Publicacion
    template_name = 'posts_list.html'
    context_object_name = 'publicaciones'

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'publicacion_form.html'
    success_url = reverse_lazy('publicacion-listar')

class PublicacionDeleteView(DeleteView):
    model = Publicacion
    template_name = 'publicacion_confirm_delete.html'
    success_url = reverse_lazy('publicacion-listar')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('/') 
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
