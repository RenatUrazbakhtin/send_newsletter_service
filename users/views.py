import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, ListView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_urlsafe(nbytes=8)

        user.token = token
        activate_url = reverse('users:email_verified', kwargs={'token': user.token})
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения регистрации перейдите по ссылке: '
                    f'http://localhost:8000/{activate_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()
        return redirect('users:email_sent')

class UserConfirmEmailView(View):
    def get(self, request, token):
        user = User.objects.get(token=token)

        user.is_active = True
        user.token = None
        user.save()
        return redirect('users:login')

class EmailConfirmationSentView(TemplateView):
    template_name = 'users/email_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    def get_object(self, queryset=None):
        return self.request.user

def generate_password(request):
    new_password = secrets.token_hex(nbytes=8)
    request.user.set_password(new_password)
    request.user.save()

    send_mail(
        subject='Смена пароля',
        message=f'Вы зарегистрировали новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))

class UserListView(LoginRequiredMixin, ListView):
    model = User
    def get_context_data(self, **kwargs):
        object_list = User.objects.all()
        context_data = super().get_context_data(**kwargs)
        context_data['users'] = object_list

        return context_data

def change_activity(*args, **kwargs):
    user = get_object_or_404(User, pk=kwargs.get('pk'))
    if user.is_active:
        user.is_active=False
    else:
        user.is_active=True
    user.save()

    return redirect(reverse('users:user_list'))
