from rest_framework import serializers
from blog.models import Category, Post
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


# class PostSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'category', 'status', 'date']

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 255, validators = [UniqueValidator(queryset=Post.objects.all())])
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'status', 'date', 'category_name', 'image', 'author']

    def validate_title(self, title):
        if len(title) > 50:
            raise serializers.ValidationError("Title should not be greater than fifty")
        return title

    def get_category_name(self, obj):
        return obj.category.name
