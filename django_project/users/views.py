from django.shortcuts import render, HttpResponse, redirect # redirect: página a redirecionar
from django.contrib.auth.decorators import login_required # decorador para restringir o acesso a uma view
from django.contrib import messages # exibir mensagens
from .forms import NewUserFields, UserUpdateForm, ProfileUpdateForm # classe que herda CreateUserForm
from . import models


# forms são post requests
def register_page(request:HttpResponse):
    if request.method == 'POST':
        form = NewUserFields(request.POST) # passa os dados que foram escritos no forms
        if form.is_valid():
            form.save() # automaticamente cria o usuário
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Conta criada com sucesso. Já pode logar.')
            return redirect(to='login')
    else:
        form = NewUserFields()
    return render(request, template_name='users/register.html', context={'form':form,
                                                                         'pagetitle': 'Cadastro'})

@login_required # requere login para acessar essa página; Django automaticamente redireciona para a página que havia sido clicada antes.
def profile(request: HttpResponse):
    if request.method == 'POST':
        u_form = UserUpdateForm(data=request.POST, instance=request.user) # popula o formulário com as informações do usuário
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, message='Sua conta foi alterada com sucesso!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, template_name='users/profile.html', context=context)
