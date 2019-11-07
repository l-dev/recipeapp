from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('recipes/new', views.recipe_create, name='recipe_create'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('recipes/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:pk>/delete', views.recipe_delete, name='recipe_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete')
]