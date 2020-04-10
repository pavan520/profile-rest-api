from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HelloAPIView(APIView):
    """ Test API View"""
    def get(self,request, format=None):
        """ Return list of Features of APIView"""
        apiView =["Uses HTTP functions GET,POST,PUT,DELETE","It's a traditional Django View",
                  "Gives you most control over logic," "Is manually mapped to ur URL's"]

        return Response({"message":"Hello","features":apiView})
