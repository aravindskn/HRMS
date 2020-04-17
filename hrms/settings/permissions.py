"""
This module contains permission definitions used in the application.
"""

from rest_framework import permissions
from rest_framework.permissions import (BasePermission, IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions)


class IsAdminOrReadOnly(BasePermission):
    """
    This class defines a new permission settings to allow acess to APIs only to
    users with admin previlages.  If the user has no admin previlages, user
    will be allowed to invoke only safe methods (i.e., data retrieval).
    """

    def has_permission(self, request, view):
        return bool(
            (request.method in permissions.SAFE_METHODS and request.user.is_authenticated) or
            request.user.is_staff)


# pylint: disable=R0903
class PermissionSettings:
    """
    This class provides constants to use in applcation for the different
    levels of acess permissions.

    Attributes:
        DEFAULT_PERMISSION (IsAuthenticated): Default permission definition
        ALLOW_ANY (AllowAny): Non-Authenticated acess (anyone can access)
        IS_AUTHENTICATED (IsAuthenticated): Authenticated aceess
        IS_ADMIN_OR_READ_ONLY (IsAdminOrReadOnly): Authentications acess. Users
        without admin previlages arenot allowed to modify data.
    """

    DEFAULT_PERMISSION = IsAuthenticated
    ALLOW_ANY = AllowAny
    IS_AUTHENTICATED = IsAuthenticated
    IS_ADMIN_OR_READ_ONLY = IsAdminOrReadOnly
    IS_ADMIN = IsAdminUser


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
