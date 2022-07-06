from dataclasses import field
from rest_framework import serializers
from appapi.models import MovieUpload, Replies, Block

class MovieUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieUpload
        fields = '__all__'
        depth=1

class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = '__all__'
        depth=1

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
        depth=1