from django.urls import path
from rest_framework.authtoken import views


from api.views.doctor import DoctorView
from api.views.patient import PatientView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),



    # path(
    #     'service/',
    #     ServiceView.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     })
    # ),
    # path(
    #     'service/<int:id>/',
    #     ServiceView.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     })
    # ),
    # path(
    #     'visit/',
    #     VisitView.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     })
    # ),
    # path(
    #     'visit/<int:id>/',
    #     VisitView.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     })
    # ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
