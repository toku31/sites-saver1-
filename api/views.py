# from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from sites.models import Site, Review
from api.serializers import SiteSerializer


@api_view(['GET'])
def getRoutes(request):
  
  routes = [
      {'GET': '/api/sites'},
      {'GET': '/api/sites/id'},
      {'POST': '/api/sites/id/vote'},
      
      {'POST': '/api/users/token'},
      {'POST': '/api/users/token/refresh'}
  ]
  return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSites(request):
  print('USER:', request.user)
  sites = Site.objects.all()
  serializer = SiteSerializer(sites, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def getSite(request, pk):
  site = Site.objects.get(id=pk)
  serializer = SiteSerializer(site, many=False)
  return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def siteVote(request, pk):
  site = Site.objects.get(id=pk)
  user = request.user.profile
  data = request.data
  
  # print('DATA:', data)
  review, created = Review.objects.get_or_create(
    owner=user,
    site=site,
  )
  
  review.value = data['value']
  review.save()
  site.getVoteCount
  
  serializer = SiteSerializer(site, many=False)
  return Response(serializer.data)