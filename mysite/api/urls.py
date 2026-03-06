from django.urls import path
from . import views

urlpatterns = [
    path(
        "blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"
    ),  # class based view
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="update"
    ),
]