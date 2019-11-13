from ipware import get_client_ip

from django.db.models import Q

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


from .models import  Vote


class AnonymousUserPermission(BasePermission):

    """Custom permission class to authenticate against AnonymousUser and stop double voting """
    
    def has_permission(self, request, view):
        
        poll_pk = view.kwargs['pk']
        if request.method == "POST":
            if request.user.is_authenticated:
                if Vote.objects.filter(Q(poll=poll_pk), Q(voted_by=request.user)).exists():
                    raise PermissionDenied('Double voting disallowed')
                return True
                
            ip_address, is_routable =  get_client_ip(request)
            if Vote.objects.filter(Q(poll=poll_pk), Q(anonymous_voter__ipaddress=ip_address)).exists():
                raise PermissionDenied('Double voting disallowed')
            return True
        return True
