from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import generics
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ValidationError
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UpdateUser(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_update(self, serializer):
        if len(list(self.request.data)) == 0:
            user = self.request.user
            user.is_active = False
            user.save()
            return user
        else:
            raise ValidationError(f'Данный path запрос зарезервирован для деактивации пользователя'
                                  f' - изменять {list(self.request.data)} запрещено... '
                                  f'Отправьте пустой path запрос для деактивации пользователя')