from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from django.contrib.auth.models import User



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


class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        model1 = Movie
        fields = '__all__'


class SRDSerializer(serializers.ModelSerializer):
    average_score = serializers.IntegerField(read_only=True, default=None)


class Meta:
    model = Review
    fields = ['average_score']


class DirectorСreqteUpdateSrializer(serializers.Serializer):
    name = serializers.CharField()


class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.TimeField()
    director = serializers.IntegerField()


class ReviewCreateUpdateSerialiser(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()
    stars = serializers.IntegerField(default=5)

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValueError('polzd sush.')
        return username

class AuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
