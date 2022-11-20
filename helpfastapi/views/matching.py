from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from ..serializers import OrganizationSerializer
from ..models import Organization
from django.db.models import F

@api_view(['PUT'])
def match(request, id):
    token = request.META['HTTP_AUTHORIZATION'][13:]
    user = Token.objects.get(key=token).user
    # Get user profile from user
    # Get organization by its orgid
    # Add organization to user's matched field
    # Add organization to user's seen field
    # Return response indicating success with organization's id
    return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
def ignore(request, id):
    token = request.META['HTTP_AUTHORIZATION'][13:]
    user = Token.objects.get(key=token).user
    # Get user profile from user
    # Get organization by its orgid
    # Add organization to user's seen field
    # Return response indicating success with organization's id
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_matches(request):
    token = request.META['HTTP_AUTHORIZATION'][13:]
    user = Token.objects.get(key=token).user
    profile = user.profile

    # Get matches and serialize them
    matches = profile.matches.all()
    serializer = OrganizationSerializer(matches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def findmatch(request):
    # Get user and interests
    token = request.META['HTTP_AUTHORIZATION'][13:]
    user = Token.objects.get(key=token).user
    profile = user.profile
    interests = profile.interests

    # Get organizations
    organizations = Organization.objects.exclude(
        seenby=user.id
    ).exclude(
        isTestData=True
    ).exclude(
        approved=False
    )

    # Rank Organizations
    # Side note: this just sucks. Try to find a way to change in the future
    matches = organizations.annotate(rank=(
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
    )).order_by('rank')[:2]

    # Return highest 2 ranked organizations
    if matches.count() == 0:
        return Response({"error": "no matches found"}, status=status.HTTP_200_OK)
    match1 = OrganizationSerializer(matches[0])
    if(matches.count() > 1):
        match2 = OrganizationSerializer(matches[1])
        return Response({"current": match1.data, "next": match2.data}, status=status.HTTP_200_OK)
    else:
        return Response({"current": match1.data}, status=status.HTTP_200_OK)
