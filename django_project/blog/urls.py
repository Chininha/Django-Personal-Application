# aqui serão mapeadas todas URL's da aplicação blog específica
# Cada uma deve possuir uma função de view correspondente

from django.urls import path
from . import views


urlpatterns = [
    # path vazio = página inicial da web page.
    # aponta para qual view deve receber a response
    path('', views.home_page, name='blog-home'),
    # esse path é usado como busca após o URLConf do projeto retornar a string de comparação. Caso bata, retorna a view.
    path('about/', view=views.about_page, name='blog-about')
]
