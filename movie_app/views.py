from abc import ABC

from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import NameSerializer, AuthorizationSerializer, UserCreateSerializer
from movie_app.models import Director
from rest_framework import status
from movie_app.models import Movie
from movie_app.serializers import MovieSerializer, DirectorСreqteUpdateSrializer
from django.contrib.auth.models import User
from movie_app.serializers import Review
from movie_app.serializers import RSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView



@api_view(['GET'])
def test(request):
    direktor = {'integer': 100,
                'string': "hello",
                'boolean': True,
                'list': [
                    1, 2, 3
                ]

                }
    return Response(data=direktor)


class Direklistviewapiview(ListCreateAPIView, GenericAPIView):
    queryset = Director.objects.all()
    serializer_class = NameSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = RSerializer


class DirectorUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = NameSerializer
    lookup_field = 'id'


class MovieListDeleteUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = RSerializer
    lookup_field = 'id'


# @api_view(['GET','POST'])
# def NAME_list_view(request):
#     if request.method == 'GET':
#         name = Director.objects.all()
#         data = NameSerializer(name, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = DirectorСreqteUpdateSrializer(data=request.data)
#         if not serializer.is_valid():
#     return  Response(data={'errors':serializer.errors},
#                      status=status.HTTP_406_NOT_ACCEPTABLE)
#
# name = request.data.get('name')
# direk=Director.objects.create(name=name)
# return  Response(data=NameSerializer(direk).data,
# status=status.HTTP_201_CREATED)


# @api_view(['GET','PUT','DELETE'])
# def name_detail_view(request, id):
#     try:
#         name = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'message': 'Director not found'})
#     if request.method == 'GET':
#         data = NameSerializer(name, ).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         name.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializers = DirectorСreqteUpdateSrializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         name.name = request.data.get('name')
#         name.save()
#         return  Response (data=NameSerializer(name).data)


# @api_view(['GET','POST'])
# def Movie_list_view(request):
#     permission_classes = [permissions.IsAuthenticated]
#     if request.method == 'GET':
#         name = Movie.objects.all()
#         data = MovieSerializer(name, many=True).data
#
#         return Response(data=data)
#     elif request.method == 'POST':
#             serializer = MovieCreateUpdateSerializer(data=request.data)
#
#             if not serializer.is_valid():
#                 return Response(data={'errors': serializer.errors},
#                                 status=status.HTTP_406_NOT_ACCEPTABLE)
#
#             title = request.data.get('title')
#             description = request.data.get('description')
#             duration = request.data.get('duration')
#             director = request.data.get('director')
#
#             mv= Movie.objects.create(title=title, description=description, duration=duration, director=director)
#             return  Response(data=MovieSerializer(mv).data,status=status.HTTP_201_CREATED)
#
#
#
#
# @api_view(['GET','PUT','DELETE'])
# def MovieDetail(request, id):
#     try:
#         MVA = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data='MovieNotFound')
#     if request.method == 'GET':
#         data = MovieSerializer(MVA).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         MVA.delete()
#         return Response('no content')
#     elif request.method == 'PUT':
#         serializers = MovieCreateUpdateSerializer(data=request.data)
#         if not serializers.is_valid():
#             return Response(data={'errors': serializers.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         MVA.name = request.data.get('name')
#         MVA.save()
#         return Response(data=MovieSerializer(MVA).data)
#
#
# @api_view(['GET', 'POST'])
# def Review_list_view(request):
#     if request.method == 'GET':
#         name = Review.objects.all()
#         data = RSerializer(name, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = ReviewCreateUpdateSerialiser(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         text = request.data.get('text')
#         movie = request.data.get('movie')
#         star = request.data.get('star')
#         r=Review.objects.create(text=text, movie=movie, star=star)
#         return Response(data=RSerializer(r).data,
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def R_detail_view(request, id):
#     global name
#     try:
#         name = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         if request.method == 'GET':
#             data = RSerializer(name).data
#             return Response(data=data)
#         elif request.method == 'DELETE':
#             name.delete()
#             return Response('no content')
#         elif request.method == 'PUT':
#             serializers = ReviewCreateUpdateSerialiser(data=request.data)
#             if not serializers.is_valid():
#                 return Response(data={'errors': serializers.errors},
#                                 status=status.HTTP_406_NOT_ACCEPTABLE)
#             name.name = request.data.get('name')
#             name.save()
#         return Response(data=RSerializer(name).data)
#
#
# @api_view(['GET'])
# def RSERA(request):
#     name = Review.objects.all()
#     data = PSerializer(name, many=True).data
#     return Response(data=data)


@property
def count_reviews(self):
    return self.reviews.all().count()


@property
def rating(self):
    return Review.objects.filter(product=self).aggregate(Avg('star'))


# @api_view(['POST'])
# def authorization(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             try:
#                 token = Token.objects.get(user=user)
#             except Token.DoesNotExist:
#                 token = Token.objects.create(user=user)
#             return Response(data={'key': token.key})
#         return Response(data={'error': 'User not found'},
#                         status=status.HTTP_404_NOT_FOUND)
class AuthorizationAPIView(GenericAPIView):
    serializer_class = AuthorizationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validate_data)
        return Response(data={'message': 'Authorization'},
                        status=status.HTTP_200_OK)


# @api_view(['POST'])
# def registration(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         User.objects.create_user(username=username, password=password)
#         return Response(data={'message': 'User created!'},
#                         status=status.HTTP_201_CREATED)
class RegistrationAPIView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.data.get('username')
        request.data.get('passwor')
        User.objects.create_user(**serializer.validate_data)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)
