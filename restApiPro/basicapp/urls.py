from django.urls import path
from basicapp import views


urlpatterns = [
    path('api/',views.HelloApiView.as_view(),name='api'),
]
                                 