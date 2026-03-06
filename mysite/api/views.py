from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	# using custom view instead of generic django views
	def delete(self, request, *args, **kwargs):
		BlogPost.objects.all().delete()
		return Response(status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	lookup_field = "pk"

# Custom API View
class BlogPostList(APIView):
	def get(self, request, format=None):
		title = request.query_params.get("title", "")

		if title:
			blog_posts = BlogPost.objects.filter(title__icontains=title)
		else:
			blog_posts = BlogPost.objects.all()

		serializer = BlogPostSerializer(blog_posts, many=True)
		return Response(serializer.data, status.HTTP_200_OK)
