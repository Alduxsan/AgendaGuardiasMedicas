from rest_framework import permissions

class UpdateMisDatos(permissions.BasePermission):
    """Permite al usuario borrarse de una guardia propia"""

    def has_permission(self,request,view):
        #debo obtener la ci del objeto que se esta mirando y compararlo con el id del request
        # usuario = request.user.id
        return bool((request.method in permissions.SAFE_METHODS) and request.user and request.user.is_authenticated)
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
        '''