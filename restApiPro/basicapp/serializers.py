from rest_framework import serializers


class HelloSerializers(serializers.Serializer): 
    """Serializiers a name field for testing API view"""

    name = serializers.CharField(max_length=10)
