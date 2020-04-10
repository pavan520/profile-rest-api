from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^hellow-view',views.HelloAPIView.as_view()),
]