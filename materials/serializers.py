from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_youtube_url


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_youtube_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    counter_of_lessons = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_counter_of_lessons(self, object: Course) -> int:
        return object.lessons.count()

    def get_is_subscribed(self, object: Course) -> bool:
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return object.subscriptions.filter(user=user).exists()
