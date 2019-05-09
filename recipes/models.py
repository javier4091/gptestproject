from django.db import models

class User(models.Model): #username(unique field), email(unique field), first_name,last_name,m password.
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    m_password = models.CharField(max_length=200)
    
    def __str__(self):
        return 'username:{} , email:{} , first_name:{} , last_name:{} , m_password:{}'.format(self.username,self.email,self.first_name,self.last_name,self.m_password)
class Recipe(models.Model): #name(string, not null), Foreign Key to User table(one to one relationship), One to Many relationship with Step and Ingredient Model
    name = models.CharField(max_length=200, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return 'name:{} , user:{}'.format(self.name, self.user.email)
class Step(models.Model): #step_text(string field, not null), Many to One relationship with Recipe
    step_text = models.CharField(max_length=200, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
class Ingredient(models.Model): #text(not null, string), Many to One relationship with Recipe
    text = models.CharField(max_length=200, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)


