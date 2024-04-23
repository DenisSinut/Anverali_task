from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from app.models import User
from django import forms





class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите тип аккаунта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'type', 'email', 'password1', 'password2' ]



class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    type = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    experience = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control py-4'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'type', 'email', 'phone_number', 'experience']