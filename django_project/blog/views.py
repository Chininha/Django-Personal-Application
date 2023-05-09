from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # usado para carregar templates
from django.shortcuts import render  # usado para renderizar templates

# função que retorna o que o usuário irá ver após uma requisição.

# é preciso mapear uma URL para essa view

posts = [{'author': 'Guilherme China',
          'title': 'The 1st post',
          'content': 'Just a message from Guilherme China',
          'date_posted': 'June, 2023'},
         {'author': 'Isabela China',
          'title': 'The 2nd post',
          'content': 'Just a message from John Doe',
          'date_posted': 'July, 2023'}
         ]  # lista de dicionários


def home_page(request: render):
    # nome do subdiretório dentro da pasta templates / nome do arquivo HTML
    # ainda retorna um HttpResponse. Pode retornar uma excessão também

    # as chaves serão essenciais para acessar os dados no documento HTML
    context = {'posts': posts,
               'title': 'random title'}
    # context: permite acessar os dados no template
    return render(request, template_name='blog/home.html', context=context)

# outra maneira de renderizar o template


def about_page(request: HttpResponse):
    template = loader.get_template('blog/about_page.html')
    return HttpResponse(template.render(context={'title': 'Inserting about page'}, request=request))
