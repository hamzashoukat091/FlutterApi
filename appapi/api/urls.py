from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('movieupload', MovieUploadViewset, basename='movieupload')
router.register('replies', RepliesViewset, basename='replies')
router.register('block', BlockViewset, basename='block')


urlpatterns = [
    path('', include(router.urls))
    
]