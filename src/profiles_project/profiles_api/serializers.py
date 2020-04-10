from rest_framework import serializers


class HelloSerialize(serializers.Serializer):
    """ Serializes a name field for testing our API view"""
    name  = serializers.CharField(max_length=10)

