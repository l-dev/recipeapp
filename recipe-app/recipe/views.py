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
    recipes = Recipe.objects.get(pk=pk)
    return render(request, 'recipe/recipe_detail.html', {'recipes': recipes})
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipes = form.save()
            return redirect('recipe_detail', pk=recipes.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_form.html', {'form': form})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save()
            return redirect('recipe_detail', pk=recipes.pk)
    else:
        form = CommentForm()
    return render(request, 'recipe/comment_form.html', {'form': form})

def recipe_edit(request, pk):
    recipes = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipes)
        if form.is_valid():
            recipes = form.save()
           
            return redirect('recipe_detail', pk=recipes.pk)
    else:
        form = RecipeForm(instance=recipes)
    return render(request, 'recipe/recipe_form.html', {'form': form})
def recipe_delete(request, pk):
    Recipe.objects.get(id=pk).delete()
    return redirect('recipe_list')
def comment_delete(request,pk):
    Comments.objects.get(id=pk).delete()
    return redirect('recipe_detail')
# Create your views here.
