from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from appapi.models import *


class MovieUploadViewset(viewsets.ModelViewSet):
    serializer_class = MovieUploadSerializer

    def get_queryset(self):
        movie_data = MovieUpload.objects.all()
        return movie_data

    def create(self, request, *args, **kwargs):
        movie_data = request.data
        print(movie_data)
        new_movie = MovieUpload.objects.create(movie_name=movie_data['movie_name'],movie_url=movie_data['movie_url'])

        new_movie.save()

        serializer = MovieUpload(new_movie)
        return Response(serializer.movie_name)

class RepliesViewset(viewsets.ModelViewSet):
    serializer_class = RepliesSerializer

    def get_queryset(self):
        replies = Replies.objects.all()
        return replies

    def create(self, request, *args, **kwargs):
        replies = request.data
        print(replies)
        reply = Replies.objects.create(reply=replies['reply'])

        reply.save()

        serializer = Replies(reply)
        return Response(serializer.reply)

class BlockViewset(viewsets.ModelViewSet):
    serializer_class = BlockSerializer

    def get_queryset(self):
        block = Block.objects.all()
        return block

    def create(self, request, *args, **kwargs):
        block_data = request.data
        # print(movie_data)
        block = MovieUpload.objects.create()

        block.save()

        serializer = MovieUpload(block)
        return Response(serializer.is_active)