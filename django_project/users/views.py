from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewUserFields

def register_page(request:HttpResponse):
    if request.method == 'POST':
        form = NewUserFields(request.POST)
        if form.is_valid():
            form.save() # automaticamente cria o usuário
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'O usuário {username} foi criado com sucesso!')
            return redirect(to='/')
    else:
        form = NewUserFields()
    return render(request, template_name='users/register.html', context={'form':form,
                                                                         'pagetitle': 'Cadastro'})
