from rest_framework import serializers
from moviewiki.models import Movie, Genre, Poster

class MovieSerializer(serializers.ModelSerializer):
    genre_str = serializers.SerializerMethodField(read_only=True)
    poster_str = serializers.SerializerMethodField(read_only=True)

    class Meta:
        exclude = ["deleted_at"]
        model = Movie

    def get_genre_str(self, obj):
        if obj.genre.all().exists():
            return [genre.genre for genre in obj.genre.all()]
        return []

    def get_poster_str(self, obj):
        if obj.poster.all().exists():
            return [poster.poster_path for poster in obj.poster.all()]
        return []
    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ["deleted_at"]
        model = Genre

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ["deleted_at"]
        model = Poster