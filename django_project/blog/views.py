from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # usado para carregar templates
from django.shortcuts import render  # usado para renderizar templates
from . import models

# função que retorna o que o usuário irá ver após uma requisição.

# é preciso mapear uma URL para essa view


def home_page(request: render):
    # nome do subdiretório dentro da pasta templates / nome do arquivo HTML
    # ainda retorna um HttpResponse. Pode retornar uma excessão também

    # as chaves serão essenciais para acessar os dados no documento HTML
    context = {'posts': models.Post.objects.all(),
               'pagetitle': 'Home Page'} # acessando os dados do modelo por aqui 
    # context: permite acessar os dados no template
    return render(request, template_name='blog/home.html', context=context)

# outra maneira de renderizar o template


def about_page(request: HttpResponse):
    template = loader.get_template('blog/about_page.html')
    return HttpResponse(template.render(request=request))
