from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from rest_framework import status
from . import models
from . import permissions
from .models import ProfileFeedItem as ProfileFeedItem


# Create your views here.

class HelloAPIView(APIView):
    """ Test API View"""

    seriazler_obj = serializers.HelloSerialize

    def get(self, request, format=None):
        """ Return list of Features of APIView"""
        apiView = ["Uses HTTP functions GET,POST,PUT,DELETE", "It's a traditional Django View",
                   "Gives you most control over logic," "Is manually mapped to ur URL's"]

        return Response({"message": "Hello", "features": apiView})

    def post(self, request):
        """ Create a Hello message """
        serializer = serializers.HelloSerialize(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """Handles updating partailly an object with provided details"""
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """Handles deletion of  an object"""
        return Response({"method": "delete"})


class HelloViewSet(viewsets.ViewSet):
    """  Test API View set."""

    seriazler_obj = serializers.HelloSerialize

    def list(self, request):
        """ Hello Message"""

        a_viewset = ["Uses actions (list, create, retrieve, update, partial_update)",
                     "Automatically maps to URLs using Routers",
                     "Provide more functionality with less code"]
        return Response({"message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """ Create a new Hello Msg"""
        serializer = serializers.HelloSerialize(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = 'Hello {0}'.format(name)

            return Response({"message": message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting an object by ID """
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """ Handles updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles updating an object partially"""
        return Response({"http_method": "PATCh"})

    def destroy(self, request, pk=None):
        """ Handles removing an object """
        return Response({"http_method": "DELETE"})


class USerProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating,& updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """ Checks email n password and returns an Auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """ Use the obtainAuthToken API view to validate & create a token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, reading & updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self,serliazer):
        """ Sets the user profile to the logged in user"""
        serliazer.save(user_profile=self.request.user)

