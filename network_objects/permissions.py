from rest_framework import permissions
from rest_framework.serializers import ValidationError



class NotUpdate(permissions.BasePermission):
    """Запрет на обновление"""

    def has_permission(self, request, view):
        raise ValidationError('запрещено обновлять поле с долгом по API - воспользуйтесь админ панелью!..')



