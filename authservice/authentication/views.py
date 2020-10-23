import jwt
from django.conf import settings
from rest_framework import exceptions, generics, status, permissions
from rest_framework.response import Response

from .models import User
from .renderers import OutBoundDataRenderer
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from .tokens import ExtendedRefreshToken


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (OutBoundDataRenderer,)

    def post(self, request):
        """
        Creates a new user of the Readerlist service.

        :param request:
        :return:
        """
        # save new user if all details are valid
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # retrieve the saved user
        user = User.objects.get(email=serializer.data['email'])
        serializer = self.serializer_class(instance=user)

        # put code to send user a verification email here

        # response
        try:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise exceptions.APIException(repr(e), code=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    renderer_classes = (OutBoundDataRenderer,)

    def post(self, request):
        """
        User login API.

        :param request:
        :return:
         Returns the access and refresh tokens.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    renderer_classes = (OutBoundDataRenderer,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        User logout API.

        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = User.objects.get(username=serializer.data['username'])
        if user:
            token = serializer.data['token']
            try:
                # private_k = settings.SIMPLE_JWT['VERIFYING_KEY']
                # k = private_k if private_k else settings.SIMPLE_JWT['SIGNING_KEY']
                # payload = jwt.decode(token, key=k)
                # user = User.objects.get(id=payload['user_id'])
                sjwt_token = ExtendedRefreshToken(token)
                _, flag = sjwt_token.blacklist()
                return Response({'status': 'Successfully logged out' if flag else 'Error'},
                                status=status.HTTP_200_OK)
            except Exception as e:
                raise exceptions.APIException(repr(e), code=status.HTTP_400_BAD_REQUEST)
        else:
            raise exceptions.APIException('User could not be found, logout failed', code=status.HTTP_400_BAD_REQUEST)
