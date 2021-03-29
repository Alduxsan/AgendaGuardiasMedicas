from rest_framework import permissions

class UpdateMisGuardias(permissions.BasePermission):
    """Permite al usuario borrarse de una guardia propia"""

    def has_object_permission(self,request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        

        return obj.id == request.user.id

