# blog/forms.py

from django import forms
from .models import BlogContent, BlogPost , contact_detail 

class BlogContentForm(forms.ModelForm):
    class Meta:
        model = BlogContent
        fields = ['subtitle', 'paragraph']

class BlogPostForm(forms.ModelForm):
    contents = forms.inlineformset_factory(BlogPost, BlogContent, form=BlogContentForm, extra=1)


    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category', 'author']

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = contact_detail
        fields = ['name', 'email','subject','message']