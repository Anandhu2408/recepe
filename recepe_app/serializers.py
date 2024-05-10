from django.contrib.auth.models import User
from rest_framework import serializers
from .models import recipe,review





class recipeserializers(serializers.ModelSerializer):
    class Meta:
        model=recipe
        fields=['id','recipe_ingredients','recipe_name','instructions','cuisine','meal_type']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']


    def create(self,validate_data):
        user=User.objects.create_user(username=validate_data['username'],password=validate_data['password'])
        user.save()
        return user

class reviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['id','recipe_name','user','rating','comment']