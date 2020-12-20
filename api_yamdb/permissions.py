from rest_framework import permissions


class ReadOnlySafeMethods(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and
                obj.author == request.user)


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and
                request.user.is_moderator)

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and
                request.user.is_moderator)


class IsAdminOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and
                (request.user.is_admin or request.user.is_staff)
                )

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and
                (request.user.is_admin or request.user.is_staff)
                )
