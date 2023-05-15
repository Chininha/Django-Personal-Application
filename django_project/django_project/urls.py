from django.contrib import admin
from django.contrib.auth import views as auth_views # views para login e logout
from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

# representa as URL's que são armazenadas na variável ROOT_URLCONF no arquivo 'settings'.
# Somente as url's definidas nessa lista de pattern serão funcionais
# As URL's, quando chamadas no browser, seão buscadas aqui


# include: aponta para onde a página deve redirecionar e completa a URL daqui com a string definida no path do arquivos urls.py do app.
# recebe http://localhost:8000/. Toda a parte até "8000/" é cortada, e somente o "" é enviado.
# Caso haja um correspondente no blog/urls.py, ele trará a view.

urlpatterns = [
    path('admin/', admin.site.urls),
    # views baseadas em classes,
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register_page, name='register'), # path('register/', users.views.register_page)
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url para acessar os arquivos de upload
