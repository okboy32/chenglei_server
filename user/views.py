import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions, status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from chenglei_server.settings import REGEX_MOBILE
from user.models import VerifyCode
from user.serializers import UserSerializer

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': user.username
        })

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
            import re
            if re.match(REGEX_MOBILE,username):
                user_login_by_mobile = User.objects.filter(mobile=username).first()
                five_mins_age = datetime.datetime.now() - datetime.timedelta(minutes=5)
                code = VerifyCode.objects.filter(mobile=username, add_time__gt=five_mins_age).order_by('-add_time').first()
                if code.code == password and code and user_login_by_mobile:
                    return user_login_by_mobile
        except Exception as e:
            return None

class UserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (TokenAuthentication, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if kwargs['pk'] != str(request.user.id):
            return Response({
                'user': '无法获取他人资料'
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)