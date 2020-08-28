from django.urls import path, include
from boards.views import (
    BoardsCreateView, BoardDetailView, BoardSearchAPIView
)

urlpatterns = [
    # create a new doctor profile
    path("create/",BoardsCreateView.as_view(),name="cboard"),

    #retrieves details of the current board
    path("<str:pk>/",BoardDetailView.as_view(),name="rudboard"),

    # Search board
    path("search/", BoardSearchAPIView.as_view(), name='sboard'),
]