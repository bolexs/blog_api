from .models import *
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author_id', 'title','message', 'created_at']

        def create(self, validated_data, **kwargs):
            author_id = kwargs['author_id']
            post = super().create(dict(author_id=author_id, **validated_data))
            return post


class UpdatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','author_id', 'updated_at']


