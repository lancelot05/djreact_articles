from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls








# from django.urls import path

# from . import views as v

# urlpatterns = [
#     path('', v.ArticleListView.as_view()),
#     path('create/', v.ArticleCreateView.as_view()),
#     path('<pk>/delete/', v.ArticleDeleteView.as_view()),
#     path('<pk>/update/', v.ArticleUpdateView.as_view()),
#     path('<pk>', v.ArticleDetailView.as_view()),
    
# ]