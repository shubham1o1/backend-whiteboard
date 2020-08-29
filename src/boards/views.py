from django.shortcuts import render
from .models import Boards, Picture
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerProfile
from .serializers import BoardSerializer, PictureSerializer
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


# Board Views:
class BoardsCreateView(CreateAPIView):
    queryset= Boards.objects.all()
    serializer_class=BoardSerializer
    permission_classes=[IsOwnerProfile, IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Boards.objects.all()
    serializer_class=BoardSerializer
    permission_classes=[IsOwnerProfile, IsAuthenticated]

# Searching Boards
class BoardSearchAPIView(ListAPIView):
    search_fields = [
        'idx',
        'title',
        'user__first_name',
        'user__last_name',
        'date_created',
    ]
    filter_backends = (filters.SearchFilter,)
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer
    permission_classes=[IsOwnerProfile, IsAuthenticated]

class BoardListView(generics.ListAPIView):

    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        return Boards.objects.filter(user=user)


class PictureCreateView(CreateAPIView):
    queryset= Picture.objects.all()
    serializer_class=PictureSerializer

    def post(self, request, *args, **kwargs):
        serializer = PictureSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Picture.objects.all()
    serializer_class=PictureSerializer
    # permission_classes=[IsOwnerProfile, IsAuthenticated]

class PictureListView(generics.ListAPIView):

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer