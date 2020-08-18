from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from basicapp import serializers
from basicapp import models
from basicapp import permission

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'is mapped manually to URls',
        ]
        return Response({'message': 'HELLO','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our nam"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello '+ name
            return Response({'message' : message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

            
    def put(self,request,pk=None):
        """Handle updating a object """
        return Response({'method' : 'PUT'})
    
    def patch(self,request,pk=None):
        """Handle updating a object partially """
        return Response({'method' : 'PATCH'})
    
    def delete(self,request,pk=None):
        """Handle Delete a object """
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automaticaly maps to URLs using Routers',
            'Provides more funtionality with less code',
        ]

        return Response({'message':'Hello ','a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'hello  ' + name
            return Response({'message':message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Handle Getting an empty object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an empty object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object """
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permission.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self,serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)