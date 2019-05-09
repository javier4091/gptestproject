from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    path('recipes/GetAllRecipe/', views.RecipeList.as_view(), name='GetAllRecipes'),
    path('recipes/GetRecipeByUser/<int:user>/', views.RecipeByUser.as_view(), name='GetRecipeByUser'),
    path('recipes/AddNewRecipe/', views.AddNewRecipe.as_view(), name = 'AddNewRecipe'),
    path('recipes/AddNewStep/', views.AddNewStep.as_view(), name = 'AddNewStep'),
    path('recipes/AddNewIngredient/', views.AddNewIngredient.as_view(), name = 'AddNewIngredient'), 
    path('recipes/UpdateRecipe/<int:pk>/', views.UpdateRecipe.as_view(), name = 'UpdateRecipe'),
    path('recipes/DeleteRecipe/<int:pk>/', views.DeleteRecipe.as_view(), name = 'DeleteRecipe'),
    
    
    #path('recipes/user/', views.UserList.as_view()),
    #path('recipes/user/<int:pk>/', views.UserDetail.as_view()),
    #path('recipes/recipe/', views.RecipeList.as_view()),
    #path('recipes/recipe/<int:pk>/', views.RecipeDetail.as_view()),
    #path('recipes/step/', views.StepList.as_view()),
    #path('recipes/step/<int:pk>/', views.StepDetail.as_view()),
    #path('recipes/ingredient/', views.IngredientList.as_view()),
    #path('recipes/ingredient/<int:pk>/', views.IngredientDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)