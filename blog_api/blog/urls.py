from django.urls import path, include
from blog.views import CaregoryAPIView, PostAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, PostViewSet, CategoryViewSet
from rest_framework import routers


blog_router = routers.DefaultRouter()
blog_router.register("posts", PostViewSet)
blog_router.register("categories", CategoryViewSet)

urlpatterns = [
    path('', include(blog_router.urls)),
    # path('categories', CaregoryAPIView.as_view()),
    # path('posts', PostListCreateAPIView.as_view()),
    # path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view()),
    # path('posts', PostAPIView.as_view()),

]