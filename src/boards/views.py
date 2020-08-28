from django.shortcuts import render
from .models import Boards
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerProfile
from .serializers import BoardSerializer
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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