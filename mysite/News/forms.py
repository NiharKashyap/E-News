from django.forms import ModelForm, fields
from .models import News
from News import models


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body']

