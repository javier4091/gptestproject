from rest_framework import serializers
from .models import User, Recipe, Step, Ingredient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'm_password')
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'user')
class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('step_text', 'recipe')
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('text', 'recipe')