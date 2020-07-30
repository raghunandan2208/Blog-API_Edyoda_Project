from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import CategorySerializer, PostSerializer
from blog.models import Category, Post
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from blog.permissions import IsAuthorOrReadOnly
from blog.pagination import PostPagination
# Create your views here.

class CaregoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        ser_cat = CategorySerializer(categories, many = True)
        return Response({"categories":ser_cat.data})


# class PostAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all().select_related('category')
#         ser_post = PostSerializer(posts, many = True)
#         return Response(ser_post.data)

#     def post(self, request, *args, **kwargs):
#         cat_data = request.data.get("category")
#         try:
#             cat_obj =Category.objects.get(id = cat_data.get('id'))
#         except:
#             return Response({"errors":"Invalid Category"}, status = status.HTTP_400_BAD_REQUEST)
        
#         ser_post = PostSerializer(data = request.data)

#         if ser_post.is_valid():
#             ser_post.validated_data['category'] = cat_obj
#             post_obj = ser_post.save()
#             ser_obj = PostSerializer(post_obj)
#             return Response(ser_obj.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(ser_post.errors, status = status.HTTP_400_BAD_REQUEST)



class PostAPIView(APIView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().select_related('category')
        ser_post = PostSerializer(posts, many = True)
        return Response(ser_post.data)

    def post(self, request, *args, **kwargs):
        
        ser_post = PostSerializer(data = request.data)

        if ser_post.is_valid():
            post_obj = ser_post.save()
            ser_obj = PostSerializer(post_obj)
            return Response(ser_obj.data, status = status.HTTP_201_CREATED)
        else:
            return Response(ser_post.errors, status = status.HTTP_400_BAD_REQUEST)


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication, DjangoModelPermissions]
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissions, IsAuthorOrReadOnly]
    pagination_class = PostPagination









