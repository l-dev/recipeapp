from django import forms
from .models import Recipe, Comments

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'body', 'photo_url', 'origin')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('recipe', 'body')