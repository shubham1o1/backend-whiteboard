from django.urls import path, include
from boards.views import (
    BoardsCreateView, BoardDetailView, BoardSearchAPIView, BoardListView,
    PictureDetailView, PictureCreateView, PictureListView
)

urlpatterns = [
    # create a new doctor profile
    path("create/",BoardsCreateView.as_view(),name="cboard"),

    #retrieves details of the current board
    path("search/<str:pk>/",BoardDetailView.as_view(),name="rudboard"),

    # Search board
    path("search/", BoardSearchAPIView.as_view(), name='sboard'),

    # List Boards
    path("list",BoardListView.as_view(), name = "lboard"),

    # Save Picture
    path("savepic/",PictureCreateView.as_view(), name = 'cpic'),

    # Retrieve and update
    path("readpic/<str:pk>",PictureDetailView.as_view(), name = 'rudpic'),

    # List picture
    path("readpic/",PictureListView.as_view(), name = "lboard"),

]