from rest_framework import permissions

class CanDeleteItem(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'DELETE':
            item = view.get_object()
            if item.fetched:
                return False
        return True




class CanUpdateItem(permissions.BasePermission):
    def has_permission(self, request, view):
    
        if request.method == 'PUT':
            item = view.get_object()
            if item.fetched:
                return False
        return True