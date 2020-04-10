from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloAPIView(APIView):
    """ Test API View"""

    seriazler_obj = serializers.HelloSerialize

    def get(self,request, format=None):
        """ Return list of Features of APIView"""
        apiView =["Uses HTTP functions GET,POST,PUT,DELETE","It's a traditional Django View",
                  "Gives you most control over logic," "Is manually mapped to ur URL's"]

        return Response({"message":"Hello","features":apiView})

    def post(self,request):
        """ Create a Hello message """
        serializer = serializers.HelloSerialize(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Hello {0}'.format(name)

            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object"""
        return Response({"method":"put"})


    def patch(self,request,pk=None):
        """Handles updating partailly an object with provided details"""
        return Response({"method":"patch"})


    def delete(self,request,pk=None):
        """Handles deletion of  an object"""
        return Response({"method":"delete"})

