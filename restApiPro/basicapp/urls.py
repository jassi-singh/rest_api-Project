from django.urls import path, include
from rest_framework.routers  import DefaultRouter
from basicapp import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='helloviewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('api/',views.HelloApiView.as_view(),name='api'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('', include(router.urls)),
]
                                  