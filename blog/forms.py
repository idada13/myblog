from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    
    # provide association between the modelform and the model
    class Meta:
        model = Post
        fields = ('author','title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
