from django.urls import path, include
from .views import ArticleViewSet, article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    # path('article_detail/<int:pk>/', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('article_detail/<int:pk>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]
