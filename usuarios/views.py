from multiprocessing import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Proficional, Academica, Qualificacoes, User
from .forms import UserCreationForm

# Views de criação de objetos
class UserCreate(CreateView):
    template_name   = 'form.html'
    form_class      = UserCreationForm
    success_url     = reverse_lazy('lista-user')

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Cadastro de Usuario"
        context['botao']    = "Cadastrar"
        return context

class ProficionalCreate(LoginRequiredMixin, CreateView):
    login_url       = reverse_lazy('login')
    model           = Proficional
    fields          = ['occupation', 'company', 'functions', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-profissao')

    def form_valid(self, form):
        #Antes do objeto ser criado
        form.instance.user  = self.request.user

        url = super().form_valid(form)
        #depois do objeto ser criado
        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Experiencia profissional"
        context['botao']    = "Cadastrar"
        return context

class AcademicaCreate(LoginRequiredMixin, CreateView):
    login_url       = reverse_lazy('login')
    model           = Academica
    fields          = ['course', 'university', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-academico')

    def form_valid(self, form):
        #Antes do objeto ser criado
        form.instance.user  = self.request.user

        url = super().form_valid(form)
        #depois do objeto ser criado
        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Historico academico"
        context['botao']    = "Cadastrar"
        return context

class QualificacoesCreate(LoginRequiredMixin, CreateView):
    login_url       = reverse_lazy('login')
    model           = Qualificacoes
    fields          = ['title', 'company', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-qualificacao')

    def form_valid(self, form):
        #Antes do objeto ser criado
        form.instance.user  = self.request.user

        url = super().form_valid(form)
        #depois do objeto ser criado
        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Cadastro de Qualificações"
        context['botao']    = "Cadastrar"
        return context


# Views de atualização de objetos
class ProficionalUpdate(LoginRequiredMixin, UpdateView):
    login_url       = reverse_lazy('login')
    model           = Proficional
    fields          = ['occupation', 'company', 'functions', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-profissao')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Proficional, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Atualizar experiencia Profissional"
        context['botao']    = "Atualizar"
        return context

class AcademicaUpdate(LoginRequiredMixin, UpdateView):
    login_url       = reverse_lazy('login')
    model           = Academica
    fields          = ['course', 'university', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-academico')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Academica, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Atualizar historico academico"
        context['botao']    = "Atualizar"
        return context

class QualificacoesUpdate(LoginRequiredMixin, UpdateView):
    login_url       = reverse_lazy('login')
    model           = Qualificacoes
    fields          = ['title', 'company', 'initialDate', 'finaleDate']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-qualificacao')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Qualificacoes, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Atualizar qualificações"
        context['botao']    = "Atualizar"
        return context

class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url       = reverse_lazy('login')
    model           = User
    fields          = ['Address', 'numberFone','email', 'abstract']
    template_name   = 'form.html'
    success_url     = reverse_lazy('lista-user')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(User, pk=self.request.user.pk)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']   = "Atualizar Usuario"
        context['botao']    = "Atualizar"
        return context

# Views de exclusão de objetos
class ProficionalDelete(LoginRequiredMixin, DeleteView):
    login_url       = reverse_lazy('login')
    model           = Proficional
    template_name   = 'form-excluir.html'
    success_url     = reverse_lazy('lista-profissao')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Proficional, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

class AcademicaDelete(LoginRequiredMixin, DeleteView):
    login_url       = reverse_lazy('login')
    model           = Academica
    template_name   = 'form-excluir.html'
    success_url     = reverse_lazy('lista-academico')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Academica, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

class QualificacoesDelete(LoginRequiredMixin, DeleteView):
    login_url       = reverse_lazy('login')
    model           = Qualificacoes
    template_name   = 'form-excluir.html'
    success_url     = reverse_lazy('lista-qualificacao')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(Qualificacoes, pk=self.kwargs['pk'], user=self.request.user)
        return self.object

class UserDelete(LoginRequiredMixin, DeleteView):
    login_url       = reverse_lazy('login')
    model           = User
    template_name   = 'form-excluir.html'
    success_url     = reverse_lazy('lista-user')

    def get_object(self, queryset=None):
        self.object =   get_object_or_404(User, pk=self.request.user.pk)
        return self.object

# Views de listagem de objetos
class UserList(ListView):
    model           = User
    template_name   = 'listas/user.html'
class ProficionalList(ListView):
    model           = Proficional
    template_name   = 'listas/profissional.html'

    def get_queryset(self):
        if (self.request.user.is_superuser):
            self.object_list    = Proficional.objects.all()    
        else:
            self.object_list    = Proficional.objects.filter(user = self.request.user)

        return self.object_list

class AcademicaList(ListView):
    model           = Academica
    template_name   = 'listas/academica.html'

    def get_queryset(self):
        self.object_list    = Academica.objects.filter(user = self.request.user)

        return self.object_list

class QualificacoesList(ListView):
    model           = Qualificacoes
    template_name   = 'listas/qualificacao.html'

    def get_queryset(self):
        self.object_list    = Qualificacoes.objects.filter(user = self.request.user)

        return self.object_list
