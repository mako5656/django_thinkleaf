from django import forms
from .models import Member


class UserForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name', 'age')
        labels = {
            'name': '名前',
            'age': '年齢'
        }
        help_texts = {
            'name': '名前を入力',
            'age': '年齢を入力'
        }