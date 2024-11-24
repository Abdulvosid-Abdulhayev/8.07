from rest_framework import serializers
from .models import Topic, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at']


class TopicSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'user', 'created_at', 'comments']
