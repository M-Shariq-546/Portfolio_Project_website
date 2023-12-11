from rest_framework import serializers
from user_projects.models import Project, Tag, Review
from users_info.models import Profile


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)# Overriding for the single profile
    tag = TagSerializers(many=True)
    review = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
        
    def get_review(self, obj): #in this case obj = project model
        review = obj.review_set.all()
        serializer = ReviewSerializers(review, many=True)
        return serializer.data