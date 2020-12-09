from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    # path('article_detail/<int:pk>/', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('article_detail/<int:pk>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]
