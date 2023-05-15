from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # usado para carregar templates
from django.shortcuts import render  # usado para renderizar templates
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView)
from . import models
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostListView(ListView): # para ordenação de objetos
    model = Post # modelo que a view vai receber dados
    template_name = 'blog/home.html' # template que a classe vai usar
    context_object_name = 'posts' # é a variável que vai ser referenciada no template
    ordering = ['-date_posted'] # por qual field deve ser ordenada a lista
    # o menos serve para falar que é descending
    # não é preciso carregar o html. A class based view automaticamente busca

def about_page(request: HttpResponse):
    return render(request, template_name='blog/about_page.html', context={'pagetitle':'Sobre o Blog'})

"""
Class-based views:
-> list views, detail views, create views, update views, delete views
"""

class PostDetails(DetailView): # para detalhamento de objetos
    model = Post
    context_object_name = 'post'
    #<app>/<model>_<viewtype>.html

class CreatePostView(LoginRequiredMixin, CreateView): # para create view é #<app>/<model>_form.html
    # herda da classe que requere login também
    model = Post
    fields = ['title', 'content']
    context_object_name = 'form'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user # autor do form atual é o usuário logado. Isso é feito antes do form enviar a requisição de post
        return super().form_valid(form=form)  # verifica se o form é válido
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form=form)
    