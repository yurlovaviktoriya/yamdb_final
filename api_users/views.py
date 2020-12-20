from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api_yamdb.permissions import IsAdminOrStaff
from .models import CustomUser
from .serializers import CustomUserSerializer, EmailSerializer


class EmailValidView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        confirmation_code = default_token_generator.make_token()
        email = request.GET.get('email')
        if (email is not None) and (
                CustomUser.objects.filter(email=email).exists()
        ):
            CustomUser.objects.create(
                email=email,
                confirmation_code=confirmation_code,
                username=email
            )
            send_mail(
                'Тема письма',
                f'Ваш код подтверждения {confirmation_code}.',
                'api_yamdb@mail.com',
                [email],
                fail_silently=False,
            )
            serializer = EmailSerializer(CustomUser.objects.get(email=email))
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class JwtGetView(APIView):
    permission_classes = (AllowAny,)

    def post(self):
        email = self.request.data.get('email')
        confirmation_code = self.request.data.get('confirmation_code')
        get_object_or_404(CustomUser,
                          email=email,
                          confirmation_code=confirmation_code
                          )
        token = default_token_generator.make_token(self.request.user)
        user_details = {'token': token}
        return Response(user_details, status=status.HTTP_200_OK)


class UsernameView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminOrStaff,)
    lookup_field = 'username'

    @action(
        detail=False,
        methods=('GET', 'PATCH'),
        permission_classes=(permissions.IsAuthenticated,)
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = CustomUserSerializer(request.user)
            return Response(serializer.data)
        serializer = CustomUserSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
