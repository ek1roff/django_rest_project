from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'cat': forms.Select(attrs={'class': 'form-control'})
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if len(title) > 200:
                raise ValidationError('Длина превышает 200 символов')
            return title
