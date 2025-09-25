from rest_framework import serializers
from movies.models import Movies
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = ['id','title','genre','actors','realease_date','rate','resume']

    def get_rate(self, obj):
      rate = obj.reviews.aggregate(Avg('star'))['star__avg']
      if rate:
          return round(rate, 1)
      return None
    

class MoviesSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self,obj):
      rate = obj.reviews.aggregate(Avg('star'))['star__avg']
      if rate:
          return round(rate,1)
      return None
                

    def validate_realease_date(self,value):
        if value.year < 1990:
            raise serializers.ValidationError('Ano incorreto, no mínimo 1990')
        return value
    
    def validate_resume(self,value):
        if len(value) > 100:
            raise serializers.ValidationError('Resumo máximo de 100 caracteres')
        return value


