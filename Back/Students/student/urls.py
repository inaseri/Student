# views
from . import views

# rest framework
from rest_framework import routers

# import urls
from django.urls import path, include
from django.conf.urls import url

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('students/', views.studentList),
    url('detail/(?P<pk>[0-9]{1,3})', views.studentDetail, name='detail'),
    url('register/', views.create_auth, name='register'),
]
