from django.urls import path
from .views import StudentList, StudentDetail, StudentCreate, StudentUpdate

urlpatterns = [
    path('students/', StudentList.as_view(), name='get_students'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='get_student'),
    path('students/add/', StudentCreate.as_view(), name='add_student'),
    path('students/update/<int:pk>/', StudentUpdate.as_view(), name='update_student'),
]
