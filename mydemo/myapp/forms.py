from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class meta:
        model=User
        fields=['username','email','password1','password2']