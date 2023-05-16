from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader  # usado para carregar templates
from django.shortcuts import render  # usado para renderizar templates
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from . import models
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
    paginate_by = 3 # faz uma paginação
    # o menos serve para falar que é descending
    # não é preciso carregar o html. A class based view automaticamente busca

class UserPostListView(ListView): # para ordenação de objetos
    model = Post # modelo que a view vai receber dados
    template_name = 'blog/user_post.html' # template que a classe vai usar
    context_object_name = 'posts' # é a variável que vai ser referenciada no template
    paginate_by = 3 # faz uma paginação
    # o menos serve para falar que é descending
    # não é preciso carregar o html. A class based view automaticamente busca

    def get_queryset(self): # função que pega o usuário associado ao nome passado na URL
        user = get_object_or_404(User, username=self.kwargs.get('username')) # kwargs nesse caso representa os parâmetro passados na URL
        "Se existe, retorna o usuário, senão, retorna 404"
        return Post.objects.filter(author=user).order_by('-date_posted') # por qual field deve ser ordenada a lista) # Filtrando os posts pelo usuário do link


def about_page(request: HttpResponse):
    return render(request, template_name='blog/about_page.html', context={'pagetitle':'Sobre o Blog'})

"""
Class-based views:
-> list views, detail views, create views, update views, delete views

LoginRequiredMixin, UserPassesTestMixin: a posição desses argumentos deve sempre ser à esquerda da class-based view que a view está herdando
LoginRequiredMixin: requer que o usuário esteja logado para acessar a view
UserPassesTestMixin: requer que o usuário logado passe em um filtro para acessar a view
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
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form=form)
    
    def test_func(self): # função para verificar se determinado usuário logado passa em um teste
        post = UpdateView.get_object(self) # capta o post que está sendo atualizado
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): # função para verificar se determinado usuário logado passa em um teste
        post = UpdateView.get_object(self) # capta o post que está sendo atualizado
        if self.request.user == post.author:
            return True
        return False