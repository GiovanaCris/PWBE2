from rest_framework.permissions import BasePermission

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated == 'G' and request.user.colaborador
    
class IsGestorOuDono(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.colaborador == 'G':
            return True
        return obj.usuario == request.user