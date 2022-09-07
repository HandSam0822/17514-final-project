from xml.etree.ElementInclude import include
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name']


class MessageSerializer(serializers.ModelSerializer):
    to_user_id = UserSerializer(read_only=True)
    from_user_id = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['from_user_id', 'message', 'to_user_id', 'creation_time']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CareerPostSerializer(serializers.ModelSerializer):
    career_post_user = UserSerializer(read_only=True)

    class Meta:
        model = CareerPost
        fields = ['id', 'career_post_title', 'type', 'career_post_text', 'career_post_user', 'company_name', 'job_title', 'location',
                  'visa_sponsor', 'creation_time']                

class CoursePostSerializer(serializers.ModelSerializer):
    course_id = CourseSerializer(read_only=True)
    course_post_user = UserSerializer(read_only=True)
    
    class Meta:
        model = CoursePost
        fields = ['id', 'course_id', 'course_post_title', 'course_post_text', 
        'course_post_user', 'creation_time']        


class CareerCommentSerializer(serializers.ModelSerializer):
    career_comment_user = UserSerializer(read_only=True)
    class Meta:
        model = CareerComment
        fields = ['id', 'career_post_id', 'career_comment_text', 'career_comment_user', 'creation_time']


class CourseCommentSerializer(serializers.ModelSerializer):
    course_comment_user = UserSerializer(read_only=True)

    class Meta:
        model = CourseComment
        fields = ['id', 'course_post_id', 'course_comment_text', 'course_comment_user', 'creation_time']