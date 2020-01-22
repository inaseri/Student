from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('students/', views.studentList),
    url('detail/(?P<pk>[0-9]{1,3})', views.studentDetail, name='detail'),
]
