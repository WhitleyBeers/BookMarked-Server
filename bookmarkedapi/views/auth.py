from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookmarkedapi.models import User


@api_view(['POST'])
def check_user(request):
    """Checks to see if User has associated user\

    Method arguments:
      request -- the full http request object
    """
    uid = request.data['uid']
    user = User.objects.filter(uid=uid).first()
    
    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'profile_image_url': user.profile_image_url,
            'bio': user.bio
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    """Handles the creation of a new user for authentication
    
    Method arguments:
      request -- the full http request object
    """
    user = User.objects.create(
        uid = request.data['uid'],
        first_name = request.data['firstName'],
        last_name = request.data['lastName'],
        email = request.data['email'],
        profile_image_url = request.data['profileImageUrl'],
        bio = request.data['bio']
    )
    
    data = {
        'id': user.id,
        'uid': user.uid,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'profile_image_url': user.profile_image_url,
        'bio': user.bio
    }
    return Response(data)
