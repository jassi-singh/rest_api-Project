from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from basicapp import serializers


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