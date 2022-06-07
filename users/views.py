from rest_framework.decorators import api_view
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response

@api_view(['GET'])
def getAllUsers(request): 
    if request.method == "GET":
        all_users = CustomUser.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)

