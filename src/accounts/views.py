# src/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faz o login automático do usuário após o cadastro
            login(request, user)
            messages.success(request, "Conta criada com sucesso!")
            return redirect('/')  # Redireciona para a página principal ou dashboard
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})