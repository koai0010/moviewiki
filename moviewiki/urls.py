from django.urls import path, include
# from debug_toolbar.toolbar import debug_toolbar_urls
from moviewiki.views import movie_view, MovieViewset, GenreViewset, PosterViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movie', MovieViewset)
router.register('genre', GenreViewset)
router.register('poster', PosterViewset)

urlpatterns = [
    path('movie/', movie_view),
    path('api/', include(router.urls))
] 
# + debug_toolbar_urls()