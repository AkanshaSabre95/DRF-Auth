from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer,UserSerializer
from rest_framework import generics


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer._validated_data['user']
    __, token = AuthToken.objects.create(user)

    return Response({
        'user_info' :{
            'id': user.id,
            'username' : user.username,
            'email': user.email,

        },
        'token' : token
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info' :{
            'id': user.id,
            'username' : user.username,
            'email': user.email,

            },
        })

    return Response({'error': 'not authenticated'}, status=400)




        

class register_api(generics.GenericAPIView):

    serializer_class = RegisterSerializer



    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({

        "user": UserSerializer(user, context=self.get_serializer_context()).data,

        "token": AuthToken.objects.create(user)[1]

        })
