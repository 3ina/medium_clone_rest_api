from django.urls import path

from .views import (
    FollowAPIView,
    FollowerListView,
    ProfileDetailAPIView,
    ProfileListAPIView,
    UnfollowAPIView,
    ProfileUpdateAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="my-profile"),
    path("me/update/", ProfileUpdateAPIView.as_view(), name="update-profile"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow/", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow/", UnfollowAPIView.as_view(), name="unfollow"),
]