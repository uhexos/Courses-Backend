from .models import Course,Lesson
from rest_framework import generics
from .serializers import CourseSerializer,LessonSerializer
# Create your views here.

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
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