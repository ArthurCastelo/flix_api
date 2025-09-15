from django.contrib import admin
from movies.models import Movies


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','realease_date','resume')
    

        
