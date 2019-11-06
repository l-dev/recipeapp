from django.shortcuts import render, redirect
from .models import Recipe, Comments
from .forms import RecipeForm, CommentForm

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})
def comment_list(request):
    comments = Comments.objects.all()
    return render(request, 'recipe/comment_list.html', {'comments': comments})
def recipe_detail(request, pk):
    recipes = Recipe.objects.get(id=pk)
    return render(request, 'recipe/recipe_detail.html', {'recipes': recipes})
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_form.html', {'form': form})
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'recipe/comment_form.html', {'form': form})
# Create your views here.
