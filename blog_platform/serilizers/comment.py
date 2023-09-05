from rest_framework import serializers

from ..models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user', "post_id", "text",]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', "post_id", "text",]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user', "post_id", "text" ]


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']