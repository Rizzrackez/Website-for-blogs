from django import forms
from home.models import *
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'post', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'input_textinput'}),
            'post': forms.Textarea(attrs={'placeholder': 'Enter content text', 'class': 'input_textarea'}),

        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['post'].label = ''
        self.fields['tags'].label = ''


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'input_textinput'}),
            'post': forms.Textarea(attrs={'placeholder': 'Enter content text', 'class': 'input_textarea'}),

        }

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['post'].label = ''


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Comment text', 'class': 'input_comments_area'}),

        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''

