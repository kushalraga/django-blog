from django import forms 
from . import models 

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ['title', 'body', 'slug', 'featured_image']