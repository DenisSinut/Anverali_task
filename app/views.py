from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView

from app.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from app.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import CommonMixin

class IndexView(CommonMixin, TemplateView):
    template_name = 'index.html'
    title = 'Платформа'

class UserLoginView(CommonMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegisterView(CommonMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы'
    title = 'Регистрация'

class UserPofileView(CommonMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.id])

def logout_view(request):
    logout(request)
    return redirect('/')