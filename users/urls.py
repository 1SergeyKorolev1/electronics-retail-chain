from django.urls import path
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UpdateUser)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(permission_classes=(AllowAny,)), name="register"),
    path("exit/<int:pk>/", UpdateUser.as_view(permission_classes=(IsAuthenticated, )), name="exit"),
    path("token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]
