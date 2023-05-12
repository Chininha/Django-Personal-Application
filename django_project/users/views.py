from django.shortcuts import render, HttpResponse, redirect # redirect: página a redirecionar
from django.contrib.auth.decorators import login_required # decorador para restringir o acesso a uma view
from django.contrib import messages # exibir mensagens
from .forms import NewUserFields # classe que herda CreateUserForm
from . import models

def register_page(request:HttpResponse):
    if request.method == 'POST':
        form = NewUserFields(request.POST)
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
    imagem = models.Profile()
    link = imagem.image.url
    return render(request, template_name='users/profile.html', context=link)
