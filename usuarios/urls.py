from django.urls import path
from django.contrib.auth import views as authViews

from .views import ProficionalCreate, AcademicaCreate, QualificacoesCreate, UserCreate
from .views import ProficionalUpdate, AcademicaUpdate, QualificacoesUpdate, UserUpdate
from .views import ProficionalDelete, AcademicaDelete, QualificacoesDelete, UserDelete
from .views import ProficionalList, AcademicaList, QualificacoesList, UserList

#Padrões de URL
urlpatterns = [
    #Caminhos de cadastro de objetos
    path('cadastro/user/', UserCreate.as_view(), name='cadastrar-user'),
    path('cadastro/profissoes/', ProficionalCreate.as_view(), name='cadastrar-profissao'),
    path('cadastro/academica/', AcademicaCreate.as_view(), name='cadastrar-academico'),
    path('cadastro/qualificacao/', QualificacoesCreate.as_view(), name='cadastrar-qualificacao'),

    #caminhos de atualização de objetos
    path('atualizar/profissoes/<int:pk>/', ProficionalUpdate.as_view(), name='atualizar-profissao'),
    path('atualizar/academica/<int:pk>/', AcademicaUpdate.as_view(), name='atualizar-academico'),
    path('atualizar/qualificacao/<int:pk>/', QualificacoesUpdate.as_view(), name='atualizar-qualificacao'),
    path('atualizar/user/', UserUpdate.as_view(), name='atualizar-user'),

    #caminhos de excluir de objetos
    path('excluir/profissoes/<int:pk>/', ProficionalDelete.as_view(), name='excluir-profissao'),
    path('excluir/academica/<int:pk>/', AcademicaDelete.as_view(), name='excluir-academico'),
    path('excluir/qualificacao/<int:pk>/', QualificacoesDelete.as_view(), name='excluir-qualificacao'),
    path('excluir/user/', UserDelete.as_view(), name='excluir-user'),

    #Caminhos de cadastro de objetos
    path('listar/user/', UserList.as_view(), name='lista-user'),
    path('listar/profissoes/', ProficionalList.as_view(), name='lista-profissao'),
    path('listar/academica/', AcademicaList.as_view(), name='lista-academico'),
    path('listar/qualificacao/', QualificacoesList.as_view(), name='lista-qualificacao'),

    #Caminhos de autenticação
    path('login/', authViews.LoginView.as_view(
        template_name = 'form_auth.html'
    ), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout')
]