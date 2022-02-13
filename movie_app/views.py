from  rest_framework.decorators import api_view
from  rest_framework.response import Response
from  movie_app.serializers import NameSerializer
from  movie_app.models import Director
from  rest_framework import status
from  movie_app.models import Movie
from  movie_app.serializers import MovieSerializer
from movie_app.serializers import Review
from movie_app.serializers import RSerializer

@api_view(['GET'])
def test(request):
    direktor= {'integer':100,
               'string': "hello",
               'boolean':True,
               'list':[
                   1,2,3
               ]

    }
    return  Response(data=direktor)
@api_view(['GET'])
def NAME_list_view(request):
    name = Director.objects.all()
    data = NameSerializer(name,many=True).data
    return  Response(data=data)


@api_view (['GET'])
def name_detail_view(request,id):
    try:
        name= Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'Director not found'})
    data = NameSerializer(name,).data
    return Response(data=data)
@api_view (['GET'])
def Movie_list_view(request):
    name = Movie.objects.all()
    data = MovieSerializer(name,many=True).data
    return  Response(data=data)
@api_view (['GET'])
def Movie_detail_view(request,id):
    try:
        name= Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'MOvie not found'})
    data = MovieSerializer(name,).data
    return Response(data=data)


@api_view(['GET'])
def Review_list_view(request):
    name = Review.objects.all()
    data = RSerializer(name,many=True).data
    return  Response(data=data)

@api_view (['GET'])
def R_detail_view(request,id):
    try:
        name= Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message':'MOvie not found'})
    data = RSerializer(name,).data
    return Response(data=data)