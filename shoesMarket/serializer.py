from rest_framework import serializers

from .models import CommentModel, ShoesModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['title', 'text', 'text', 'like', 'createdTime']

class ShoesDetailSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    shoes = CommentSerializer(many=True)

    class Meta:
        model = ShoesModel
        fields = ['gender', 'mark', 'size', 'count', 'price', 'discount', 'categoryImage', 'createdTime', 'shoes']

    def get_gender(self, obj):
        return obj.get_gender_display()

class ShoesListSerializer(serializers.HyperlinkedModelSerializer):
    commentsCount = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()

    class Meta:
        model = ShoesModel
        fields = ['gender', 'mark', 'size', 'count', 'commentsCount', 'url']

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_commentsCount(self, obj):
        return 'coumments count is {}'.format(obj.shoes.count())