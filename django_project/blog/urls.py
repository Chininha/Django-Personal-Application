# aqui serão mapeadas todas URL's da aplicação blog específica
# Cada uma deve possuir uma função de view correspondente

from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetails,
                    CreatePostView,
                    PostUpdateView
                )


urlpatterns = [
    # path vazio = página inicial da web page.
    # aponta para qual view deve receber a response
    path('', PostListView.as_view(), name='blog-home'),
    # class-based views procuram por templates com um padrão de nomenclatura
    # esse path é usado como busca após o URLConf do projeto retornar a string de comparação. Caso bata, retorna a view.
    path('about/', view=views.about_page, name='blog-about'),
    path('post/<int:pk>/', PostDetails.as_view(), name='post-detail'), # url dinâmica com url
    path('post/create',view=CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update', view=PostUpdateView.as_view(), name='post-update')
]   

#<app>/<model>_<viewtype>.html