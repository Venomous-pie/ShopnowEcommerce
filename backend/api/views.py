from serializers import RegisterUser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_user(request):
    serializer = RegisterUser(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'success': True}, status=201)