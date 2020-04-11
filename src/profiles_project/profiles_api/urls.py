from django.conf.urls import url
from . import views
from  django.conf.urls import  include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset",views.HelloViewSet, 'hello-viewset')

urlpatterns=[
    url(r'^hellow-view',views.HelloAPIView.as_view()),
    url(r'',include(router.urls))
]