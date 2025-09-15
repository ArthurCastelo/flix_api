from rest_framework import serializers
from movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self,obj):
        return 5

    def validate_realease_date(self,value):
        if value.year < 1990:
            raise serializers.ValidationError('Ano incorreto, no mínimo 1990')
        return value
    
    def validate_resume(self,value):
        if len(value) > 100:
            raise serializers.ValidationError('Resumo máximo de 100 caracteres')
        return value

