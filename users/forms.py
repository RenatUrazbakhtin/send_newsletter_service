from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserForm(UserChangeForm):
    """
    Форма для редактирования пользователя
    """
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar')

