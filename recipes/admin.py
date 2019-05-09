from django.contrib import admin

# Register your models here.
from .models import User
from .models import Recipe
from .models import Step
from .models import Ingredient

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
