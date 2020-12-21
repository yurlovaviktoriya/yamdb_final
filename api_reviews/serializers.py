from rest_framework import serializers

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        model = Review
        read_only_fields = ('pub_date',)

    def create(self, validated_data):
        author = validated_data['author']
        title = validated_data['title']

        if (self.context['request'].stream.method == 'POST'
                and Review.objects.filter(author=author, title=title).exists()):
            raise serializers.ValidationError('Отзыв уже существует')
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date',)
        model = Comment
        read_only_fields = ('pub_date',)
