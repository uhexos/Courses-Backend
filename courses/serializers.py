from rest_framework import serializers
from .models import Course,Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.PrimaryKeyRelatedField(many=True,queryset=Lesson.objects.filter(course=None))
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'pub_date', 'lessons']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description','position']