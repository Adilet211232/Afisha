from rest_framework import serializers
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class RSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
