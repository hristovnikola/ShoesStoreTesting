from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ShoesStoreApp.models import Shoes


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control mb-3"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ShoesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShoesForm, self).__init__(*args, **kwargs)
        # self.fields['emp_code'].required = False
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control mb-3"

    class Meta:
        model = Shoes
        fields = '__all__'
