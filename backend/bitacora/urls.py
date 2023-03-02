
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authorized-travels', views.AuthorizedTravelViewSet)
router.register(r'employees', views.EmployeeProfileViewSet)
router.register(r'travel-expenses', views.TravelExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


