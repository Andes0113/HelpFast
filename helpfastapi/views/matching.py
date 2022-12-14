from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from ..serializers import OrganizationSerializer, ProfileSerializer, Profile
from ..models import Categories, Organization
from .locate import get_nearby_organizations
from django.db.models import F

@api_view(['PUT'])
def match(request, id):
    auth = request.headers['Authorization']
    token = auth[13:]
    user = Token.objects.get(key=token).user
    profile = user.profile
    organization = Organization.objects.get(id=id)
    profile.matches.add(organization)
    profile.seen.add(organization)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def ignore(request, id):
    token = request.headers['Authorization'][13:]
    user = Token.objects.get(key=token).user
    profile = user.profile
    organization = Organization.objects.get(id=id)
    profile.seen.add(organization)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_matches(request):
    token = request.headers['Authorization'][13:]
    user = Token.objects.get(key=token).user
    profile = user.profile

    # Get matches and serialize them
    matches = profile.matches.all()
    serializer = OrganizationSerializer(matches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def findmatch(request):
    # Get user and interests
    token = request.headers['Authorization'][13:]
    user = Token.objects.get(key=token).user
    profile = user.profile
    interests = profile.interests

    # Get organizations
    organizations = get_nearby_organizations(
        profile.latitude, 
        profile.longitude,
        profile.settings.viewRadius
    ).exclude(
        seenby=profile
    ).exclude(
        isTestData=True
    ).exclude(
        approved=False
    )

    # Rank Organizations
    matches = calculate_ranks(organizations, interests).order_by('-rank')
    if matches.count == 0:
        return Response({"Error": "No Matches Found"}, status=status.HTTP_200_OK)

    serializer = OrganizationSerializer(matches[:4], many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def clearseen(request):
    try: 
        token = request.headers['Authorization'][13:]
        user = Token.objects.get(key=token).user
        profile = user.profile
    except Token.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    profile.seen.clear()
    profile.matches.clear()
    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)

def calculate_ranks(organizations, interests):
    # Side note: this just sucks. Try to find a way to change in the future
    return organizations.annotate(rank=(
        F('categories__arts_and_culture') * interests.arts_and_culture + 
        F('categories__charity') * interests.charity +
        F('categories__children') * interests.children +
        F('categories__community') * interests.community +
        F('categories__disaster_relief') * interests.disaster_relief +
        F('categories__emergency') * interests.emergency +
        F('categories__education') * interests.education +
        F('categories__environment') * interests.environment +
        F('categories__faith_based') * interests.family_support +
        F('categories__health_and_medicine') * interests.health_and_medicine +
        F('categories__housing') * interests.housing +
        F('categories__hunger') * interests.hunger +
        F('categories__legal') * interests.legal +
        F('categories__mental_health') * interests.mental_health +
        F('categories__seniors') * interests.seniors +
        F('categories__women') * interests.women +
        F('categories__wildlife') * interests.wildlife +
        F('categories__finance') * interests.finance +
        F('categories__nonprofit') * interests.nonprofit
    ))
