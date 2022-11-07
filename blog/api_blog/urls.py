from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('posts', PostViewSet.as_view({
        'post': 'create', 'get': 'list'
    }), name='post-list'),
    path('post/<int:pk>', PostViewSet.as_view ({
        'get':'retrieve', 'patch':'update', 'delete': 'destroy'
    }), name='post-detail')
]