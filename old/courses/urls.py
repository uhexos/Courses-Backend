from django.urls import path
from . import views
urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('courses/<int:pk>/lessons/',views.LessonList.as_view(), name='lesson-list'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
