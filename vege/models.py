from django.db import models
#for authantication system.
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    # database level par null store hota hai if there is no user, and blank true means user can submit form vacant as well
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True , blank=True)
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to = 'Recipe')
    recipe_view_count = models.IntegerField(default=1)