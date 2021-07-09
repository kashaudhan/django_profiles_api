from rest_framework import authentication
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
  """Test API View"""
  serializer_class = serializers.HelloSerializers

  def get(self, request, format=None):
    """Resturns a list of APIVIew features"""
    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)'
      'Is similar toa traditional Django view',
      'Gives you the most control',
      'Is mapped manually to URLs'
    ]

    return Response({'message': 'Hello', 'an_apiview': an_apiview})

  def post(self, request):
    """Create a hello msg with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      massage = f'Hello {name}'
      return Response({'message': massage})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
  def put(self, request, pk=None):
    """Handle updating an object"""
    return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
    """Handle patch request"""
    return Response({'method': 'PATCH'})
  
  def delete(self, request, pk=None):
    """Delete and object"""
    return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
  """Test api viewSet"""
  serializer_class = serializers.HelloSerializers

  def list(self, request):
    """return a hello msg"""
    a_viewset = [
      'Uses actions (list, create, retreive, update, partial_update)',
      'Automatically maps to URLs using Routers',
      "Provides more functionality with less code"
    ]

    return Response({'message': 'Hello!', 'a_viewset': a_viewset})

  def create(self, request):
    """Create a new hello msg"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
      )

  def retreive(self, request, pk=None):
    """Handle getting an object by its ID"""
    return Response({'http_method': 'GET'})

  def update(self, request, pk=None):
    """Handle updating an object"""
    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    """Handle updating part of an object"""
    return Response({'http_method': 'PATCH'})

  def destroy(self, request, pk=None):
    """Handle delete object"""
    return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating profiles"""
  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  