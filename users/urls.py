from django.urls import path

from django.contrib.auth import views

from main.views import HomeView

from users.views import RegisterView, UserConfirmEmailView, EmailConfirmationSentView, UserUpdateView, \
    generate_password, UserListView, change_activity

app_name = 'users'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', views.LoginView.as_view(template_name='users/login.html',), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-email/<str:token>/', UserConfirmEmailView.as_view(), name='email_verified'),
    path('email-sent/', EmailConfirmationSentView.as_view(), name='email_sent'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/changed_password/', generate_password, name='changed_password'),
    path('user_list', UserListView.as_view(), name='user_list'),
    path('change_activity/<int:pk>/', change_activity, name='change_activity'),
]