import instance as instance
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


