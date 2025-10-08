from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user




# accounts/views.py
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSimpleSerializer, FollowSerializer

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)

class FollowersListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSimpleSerializer

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['user_id'])
        return user.followers.all()

class FollowingListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSimpleSerializer

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['user_id'])
        return user.following.all()
