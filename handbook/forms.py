
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.db.models import fields
 
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

class RegistrForm(UserCreationForm):

  email = forms.EmailField(max_length=254, help_text='This field is required')
  

  class Meta:

    model = User
    fields = ('username', 'email', 'password1', 'password2', )

class CompForm(forms.ModelForm):
    
  class Meta:
    model=Company
    # company_name = forms.CharField(label='Your name', max_length=100)
    company_name = forms.CharField(label='First name',
                             max_length=30,
                             required=False)
    fields=('company_name','company_about','comapny_category','company_email','company_phone','company_logo','company_video',)
    

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )
    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )
    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )
    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )
    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #     self.helper.add_input(Submit('submit', 'Submit'))




class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': '',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': '',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': '',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': '',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': '',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UploadFileForm(forms.Form):
    file = forms.FileField()