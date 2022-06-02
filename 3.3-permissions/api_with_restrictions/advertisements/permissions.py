from rest_framework.permissions import BasePermission
from advertisements.models import Advertisement


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator
