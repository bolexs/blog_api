from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import PostSerializer, UpdatePostSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    serializer_class= PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer
        user = request.user

        if serializer.is_valid():
            post = serializer.create(serializer.validated_data, author_id=user)
            read_serializer = self.get_serializer(post)
            return Response(
                read_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return Post.objects.all()


    def get_object(self):
        id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=id)
        return post

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = UpdatePostSerializer(instance=post, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        post_instance = serializer.update(post, serializer.validated_data)
        response_data = self.get_serializer(post_instance).data
        return Response(response_data, status=status.HTTP_200_OK)


    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        deleted = f'{post} has been deleted'
        return Response(deleted, status=status.HTTP_204_NO_CONTENT)