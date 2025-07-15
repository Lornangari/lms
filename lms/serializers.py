from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from .models import Course, Enrollment
from .models import Announcement
from .models import Assignment
from .models import Submission


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')




class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()  # Or use UserSerializer if needed

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'created_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), source='course', write_only=True
    )

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'course_id', 'enrolled_at']
        read_only_fields = ['student', 'enrolled_at']


class AnnouncementSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = Announcement
        fields = ['id', 'course', 'title', 'message', 'created_at', 'posted_by']



class AssignmentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'description', 'due_date', 'created_at', 'created_by']


class SubmissionSerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField()
    student = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'content', 'submitted_at', 'grade', 'feedback']
        read_only_fields = ['student', 'submitted_at', 'assignment', 'student']




