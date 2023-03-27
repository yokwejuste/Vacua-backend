from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsHOD(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_hod == request.user.is_hod


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_admin == request.user.is_admin


class IsClassCoordinator(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_cc == request.user.is_cc


class IsDirector(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.is_director == request.user.is_director
