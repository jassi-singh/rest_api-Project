from django.urls import path, include
from rest_framework.routers  import DefaultRouter
from basicapp import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='helloviewset')


urlpatterns = [
    path('api/',views.HelloApiView.as_view(),name='api'),
    path('', include(router.urls)),
]
                                  