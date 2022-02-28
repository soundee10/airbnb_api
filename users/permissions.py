from rest_framework.permissions import BasePermission

class IsSelf(BasePermission):
    # has permission
    # has object permission v --> want to get access to the object
    def has_object_permission(self, request, view, user):
        return user == request.user