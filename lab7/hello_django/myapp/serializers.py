from myapp.models import Creator, Post
from rest_framework import serializers

class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ["id", "name", "nickname", "email"]

# class FilmSerializer(serializers.ModelSerializer):
#     directors = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Film
#         fields = ["id", "name", "original_name", "year", "directors"]