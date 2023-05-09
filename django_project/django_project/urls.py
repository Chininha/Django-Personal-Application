"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# representa as URL's que são armazenadas na variável ROOT_URLCONF no arquivo 'settings'.
# Somente as url's definidas nessa lista de pattern serão funcionais
# As URL's, quando chamadas no browser, seão buscadas aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    # include: aponta para onde a página deve redirecionar e completa a URL daqui com a string definida no path do arquivos urls.py do app.

    # recebe http://localhost:8000/. Toda a parte até "8000/" é cortada, e somente o "" é enviado.
    # Caso haja um correspondente no blog/urls.py, ele trará a view.
    path('', include('blog.urls'))
]
