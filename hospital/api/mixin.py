from rest_framework import viewsets
from api.permissions import RoleBasePermissionsMixin, HasPermissionByAuthenticatedUserRole


class HospitalGenericViewSet(
    RoleBasePermissionsMixin,
    viewsets.GenericViewSet
):
    permission_classes = [HasPermissionByAuthenticatedUserRole,]

    # pagination_class = [CustomPagination, ]

