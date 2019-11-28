from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Course, Lesson
from .permissions import IsProfileOwnerOrReadOnly
from .serializers import CourseSerializer, LessonSerializer, UserSerializer


class CourseList(generics.ListCreateAPIView):
    # get all existing courses and make new ones
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    #get a single course from all the courses
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonList(generics.ListCreateAPIView):
    # queryset =  Lesson.objects.filter()
    serializer_class = LessonSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # GET PK FROM URL USING KWARGS TO URL DEFINTIIION
        pk = self.kwargs['pk']
        return Lesson.objects.filter(course__id=pk)
     
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        course = Course.objects.get(id=pk)
        serializer.save(course=course)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsProfileOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    