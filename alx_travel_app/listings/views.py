from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.response import Response
# Create your views here.

class BookView(viewsets.ViewSets):
    """Manually creating view for Listing model."""
    def list(self, request):
        """Retrieves all Listings."""
        query_set = Listing.objects.all()
        serializer = ListingSerializer(query_set)
        return Response({'lisitngs': serializer.data})

